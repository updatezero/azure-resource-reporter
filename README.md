# Azure Resource Reporter

A Python command-line reporting tool for Azure cloud resources.

The project can connect to a real Azure subscription via the Azure SDK and report on live resources (resource groups, VMs, storage accounts, VNets, and more), including real VM power state. If no Azure subscription is configured, it falls back to local sample JSON data, so the tool always runs standalone. It is designed as a practical automation project for Cloud Engineering, Azure administration, and Cloud Security learning.

## Features

- Load resources live from an Azure subscription via the Azure SDK, with automatic fallback to local sample JSON data
- Show all resources
- Filter resources by type
- Filter resources by Azure location
- Show a summary report
- Check tag compliance
- Show security findings
- Export resources to CSV
- Export a full report to Markdown

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
- [Azure CLI](https://learn.microsoft.com/cli/azure/install-azure-cli) (only needed for live mode, to authenticate via `az login`)

Python dependencies are listed in `requirements.txt`:

- `azure-identity`
- `azure-mgmt-resource`
- `azure-mgmt-compute`

## Installation

Clone the repository:

```bash
git clone https://github.com/updatezero/azure-resource-reporter.git
cd azure-resource-reporter
pip3 install -r requirements.txt
```

Run the application with local sample data:

```bash
python3 main.py
```

### Live mode (real Azure subscription)

Authenticate once via the Azure CLI:

```bash
az login
```

Then set your subscription ID as an environment variable before running:

```bash
export AZURE_SUBSCRIPTION_ID=<your-subscription-id>
python3 main.py
```

If authentication fails or no subscription ID is set, the tool automatically falls back to the local sample data in `data/azure_resources.json`.

## Usage

```text
1. Show All Resources
2. Filter by Resource Type
3. Filter by Location
4. Show Summary
5. Check Tag Compliance
6. Show Security Findings
7. Export to CSV
8. Export to Markdown
9. Exit
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
|-- azure_client.py
|-- requirements.txt
|-- .gitignore
`-- README.md
```

## Why This Project Matters

Cloud Engineers need to collect, filter, and report on real cloud resource state — spotting missing tags, ungoverned resource groups, and security findings across a subscription. This project does that against a real Azure subscription via the Azure SDK (`azure-identity` + `azure-mgmt-resource` + `azure-mgmt-compute`), while still working standalone against local sample data for anyone without Azure access.

## Roadmap

Possible future improvements:

- Add command-line arguments
- Export security findings to CSV
- Add automated tests
- Expand live resource fields (e.g. real environment detection via Azure Policy/Management Groups)
