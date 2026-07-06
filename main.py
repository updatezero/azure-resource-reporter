import csv
import json

RESOURCE_FILE = "data/azure_resources.json"
REPORT_FILE = "azure_report.csv"
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
        tags = resource.get("tags", {})
        missing_tags = []

        for required_tag in REQUIRED_TAGS:
            if required_tag not in tags:
                missing_tags.append(required_tag)

        if missing_tags:
            non_compliant_resources += 1
            print(f"\nResource: {resource['name']}")
            print(f"Missing tags: {', '.join(missing_tags)}")
        else:
            compliant_resources += 1

    print("\nCompliance Summary")
    print(f"Compliant Resources: {compliant_resources}")
    print(f"Non-Compliant Resources: {non_compliant_resources}")


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
        print("6. Export to CSV")
        print("7. Exit")

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
            export_to_csv(resources)

        elif choice == "7":
            print("\nGoodbye!")
            break

        else:
            print("\nInvalid option. Please try again.")


if __name__ == "__main__":
    main()
