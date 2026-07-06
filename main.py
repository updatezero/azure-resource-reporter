import csv
import json
import os

from azure_client import fetch_live_resources

RESOURCE_FILE = "data/azure_resources.json"
REPORT_FILE = "azure_report.csv"
REPORT_MD_FILE = "azure_report.md"
REQUIRED_TAGS = [
    "owner",
    "cost_center",
    "environment"
]

RESOURCE_FIELDS = [
    "name",
    "resource_type",
    "resource_group",
    "location",
    "subscription",
    "environment",
    "status"
]


def load_resources():
    subscription_id = os.environ.get("AZURE_SUBSCRIPTION_ID")

    if subscription_id:
        try:
            print(f"\nFetching live resources from Azure subscription {subscription_id}...")
            return fetch_live_resources(subscription_id)
        except Exception as error:
            print(f"\nCould not fetch live Azure resources: {error}")
            print("Falling back to local sample data.")

    try:
        with open(RESOURCE_FILE, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"\nResource file not found: {RESOURCE_FILE}")
        return []


def print_resource(resource):
    print("----------------------------------------")
    print(f"Name: {resource['name']}")
    print(f"Type: {resource['resource_type']}")
    print(f"Resource Group: {resource['resource_group']}")
    print(f"Location: {resource['location']}")
    print(f"Subscription: {resource['subscription']}")
    print(f"Environment: {resource['environment']}")
    print(f"Status: {resource['status']}")


def show_resources(resources):
    print("\n=== Azure Resources ===")

    if not resources:
        print("No resources found.")
        return

    for index, resource in enumerate(resources, start=1):
        print(f"\nResource #{index}")
        print_resource(resource)


def filter_by_type(resources):
    print("\n=== Filter by Resource Type ===")

    resource_type = input("Enter resource type to search: ").lower()
    matches = []

    for resource in resources:
        if resource_type in resource["resource_type"].lower():
            matches.append(resource)

    show_resources(matches)


def filter_by_location(resources):
    print("\n=== Filter by Location ===")

    location = input("Enter Azure location to search: ").lower()
    matches = []

    for resource in resources:
        if location in resource["location"].lower():
            matches.append(resource)

    show_resources(matches)


def show_summary(resources):
    print("\n=== Azure Resource Summary ===")

    if not resources:
        print("No resources found.")
        return

    total_resources = len(resources)
    production_resources = 0
    development_resources = 0
    running_resources = 0
    stopped_resources = 0

    resource_types = {}

    for resource in resources:
        environment = resource["environment"].lower()
        status = resource["status"].lower()
        resource_type = resource["resource_type"]

        if environment == "production":
            production_resources += 1
        elif environment == "development":
            development_resources += 1

        if status == "running":
            running_resources += 1
        elif status == "stopped":
            stopped_resources += 1

        if resource_type not in resource_types:
            resource_types[resource_type] = 0

        resource_types[resource_type] += 1

    print(f"Total Resources: {total_resources}")
    print(f"Production: {production_resources}")
    print(f"Development: {development_resources}")
    print(f"Running: {running_resources}")
    print(f"Stopped: {stopped_resources}")

    print("\nResources by Type:")
    for resource_type, count in resource_types.items():
        print(f"- {resource_type}: {count}")


def check_tag_compliance(resources):
    print("\n=== Tag Compliance Check ===")

    if not resources:
        print("No resources found.")
        return

    compliant_resources = 0
    non_compliant_resources = 0

    for resource in resources:
        missing_tags = get_missing_tags(resource)

        if missing_tags:
            non_compliant_resources += 1
            print(f"\nResource: {resource['name']}")
            print(f"Missing tags: {', '.join(missing_tags)}")
        else:
            compliant_resources += 1

    print("\nCompliance Summary")
    print(f"Compliant Resources: {compliant_resources}")
    print(f"Non-Compliant Resources: {non_compliant_resources}")


def get_missing_tags(resource):
    tags = resource.get("tags", {})
    missing_tags = []

    for required_tag in REQUIRED_TAGS:
        if required_tag not in tags:
            missing_tags.append(required_tag)

    return missing_tags


def build_security_findings(resources):
    findings = []

    for resource in resources:
        missing_tags = get_missing_tags(resource)
        environment = resource["environment"].lower()
        resource_type = resource["resource_type"].lower()
        status = resource["status"].lower()

        if missing_tags:
            severity = "Medium"

            if environment == "production":
                severity = "High"

            findings.append({
                "resource_name": resource["name"],
                "severity": severity,
                "finding": f"Missing required tags: {', '.join(missing_tags)}"
            })

        if resource_type == "virtual machine" and status == "stopped":
            findings.append({
                "resource_name": resource["name"],
                "severity": "Low",
                "finding": "Virtual machine is stopped"
            })

    return findings


def show_security_findings(resources):
    print("\n=== Security Findings Report ===")

    if not resources:
        print("No resources found.")
        return

    findings = build_security_findings(resources)

    if not findings:
        print("No security findings found.")
        return

    for index, finding in enumerate(findings, start=1):
        print(f"\nFinding #{index}")
        print("----------------------------------------")
        print(f"Resource: {finding['resource_name']}")
        print(f"Severity: {finding['severity']}")
        print(f"Finding: {finding['finding']}")

    print("\nFindings Summary")
    print(f"Total Findings: {len(findings)}")
    print(f"High: {count_findings_by_severity(findings, 'High')}")
    print(f"Medium: {count_findings_by_severity(findings, 'Medium')}")
    print(f"Low: {count_findings_by_severity(findings, 'Low')}")


def count_findings_by_severity(findings, severity):
    count = 0

    for finding in findings:
        if finding["severity"] == severity:
            count += 1

    return count


def export_to_csv(resources):
    print("\n=== Export Azure Report ===")

    if not resources:
        print("No resources found.")
        return

    with open(REPORT_FILE, "w", newline="") as file:
        writer = csv.DictWriter(file, fieldnames=RESOURCE_FIELDS)

        writer.writeheader()
        writer.writerows(resources)

    print(f"\nAzure report exported successfully to {REPORT_FILE}")


def build_markdown_report(resources):
    lines = ["# Azure Resource Report", ""]

    total_resources = len(resources)
    findings = build_security_findings(resources)
    compliant_resources = 0
    non_compliant_resources = 0

    for resource in resources:
        if get_missing_tags(resource):
            non_compliant_resources += 1
        else:
            compliant_resources += 1

    lines.append("## Summary")
    lines.append("")
    lines.append(f"- Total Resources: {total_resources}")
    lines.append(f"- Tag Compliant: {compliant_resources}")
    lines.append(f"- Tag Non-Compliant: {non_compliant_resources}")
    lines.append(f"- Security Findings: {len(findings)}")
    lines.append(f"  - High: {count_findings_by_severity(findings, 'High')}")
    lines.append(f"  - Medium: {count_findings_by_severity(findings, 'Medium')}")
    lines.append(f"  - Low: {count_findings_by_severity(findings, 'Low')}")
    lines.append("")

    lines.append("## Resources")
    lines.append("")
    lines.append("| Name | Type | Resource Group | Location | Environment | Status |")
    lines.append("|------|------|-----------------|----------|-------------|--------|")

    for resource in resources:
        lines.append(
            f"| {resource['name']} | {resource['resource_type']} | "
            f"{resource['resource_group']} | {resource['location']} | "
            f"{resource['environment']} | {resource['status']} |"
        )

    lines.append("")

    lines.append("## Security Findings")
    lines.append("")

    if not findings:
        lines.append("No security findings.")
    else:
        for finding in findings:
            lines.append(
                f"- **{finding['severity']}** – {finding['resource_name']}: "
                f"{finding['finding']}"
            )

    lines.append("")

    return "\n".join(lines)


def export_to_markdown(resources):
    print("\n=== Export Azure Report (Markdown) ===")

    if not resources:
        print("No resources found.")
        return

    report = build_markdown_report(resources)

    with open(REPORT_MD_FILE, "w") as file:
        file.write(report)

    print(f"\nAzure report exported successfully to {REPORT_MD_FILE}")


def main():
    resources = load_resources()

    print("=" * 40)
    print("Azure Resource Reporter")
    print("=" * 40)

    while True:
        print("\n1. Show All Resources")
        print("2. Filter by Resource Type")
        print("3. Filter by Location")
        print("4. Show Summary")
        print("5. Check Tag Compliance")
        print("6. Show Security Findings")
        print("7. Export to CSV")
        print("8. Export to Markdown")
        print("9. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            show_resources(resources)

        elif choice == "2":
            filter_by_type(resources)

        elif choice == "3":
            filter_by_location(resources)

        elif choice == "4":
            show_summary(resources)

        elif choice == "5":
            check_tag_compliance(resources)

        elif choice == "6":
            show_security_findings(resources)

        elif choice == "7":
            export_to_csv(resources)

        elif choice == "8":
            export_to_markdown(resources)

        elif choice == "9":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid option. Please try again.")


if __name__ == "__main__":
    main()
