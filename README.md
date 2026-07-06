# Azure Resource Reporter

A Python command-line reporting tool for Azure-style cloud resources.

The project uses sample JSON data to simulate Azure resources and generate simple reports. It is designed as a practical automation project for Cloud Engineering, Azure administration, and Cloud Security learning.

## Features

- Load Azure-style resource data from JSON
- Show all resources
- Filter resources by type
- Filter resources by Azure location
- Show a summary report
- Check tag compliance
- Show security findings
- Export resources to CSV

## Resource Fields

Each resource contains:

- Name
- Resource type
- Resource group
- Location
- Subscription
- Environment
- Status

## Requirements

- Python 3

No external packages are required. The project uses Python standard library modules:

- `json`
- `csv`

## Installation

Clone the repository:

```bash
git clone https://github.com/updatezero/azure-resource-reporter.git
cd azure-resource-reporter
```

Run the application:

```bash
python3 main.py
```

## Usage

```text
1. Show All Resources
2. Filter by Resource Type
3. Filter by Location
4. Show Summary
5. Check Tag Compliance
6. Show Security Findings
7. Export to CSV
8. Exit
```

## Example Summary

```text
=== Azure Resource Summary ===
Total Resources: 5
Production: 3
Development: 2
Running: 1
Stopped: 1

Resources by Type:
- Virtual Machine: 2
- Storage Account: 1
- Key Vault: 1
- SQL Database: 1
```

## Example Tag Compliance Check

```text
=== Tag Compliance Check ===

Resource: vm-dev-app-01
Missing tags: cost_center

Resource: kv-prod-core-01
Missing tags: owner

Resource: sql-dev-reporting-01
Missing tags: environment

Compliance Summary
Compliant Resources: 2
Non-Compliant Resources: 3
```

## Example Security Findings

```text
=== Security Findings Report ===

Finding #1
----------------------------------------
Resource: vm-dev-app-01
Severity: Medium
Finding: Missing required tags: cost_center

Finding #2
----------------------------------------
Resource: vm-dev-app-01
Severity: Low
Finding: Virtual machine is stopped

Findings Summary
Total Findings: 4
High: 1
Medium: 2
Low: 1
```

## Project Structure

```text
azure-resource-reporter/
|-- data/
|   `-- azure_resources.json
|-- main.py
|-- .gitignore
`-- README.md
```

## Why This Project Matters

Cloud Engineers often need to collect, filter, and report cloud resource information. This project practices those same ideas with a simple local dataset before connecting to real Azure APIs or Azure CLI output.

## Roadmap

Possible future improvements:

- Add command-line arguments
- Add Azure CLI JSON import
- Add Azure SDK integration
- Export security findings to CSV
- Add automated tests
