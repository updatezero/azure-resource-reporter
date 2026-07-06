# Sample Live Azure Report

_Generated against a real Azure subscription via the Azure SDK. Subscription/tenant IDs redacted for the public repo._

## Summary

- Total Resources: 26
- Tag Compliant: 0
- Tag Non-Compliant: 26
- Security Findings: 26
  - High: 0
  - Medium: 26
  - Low: 0

## Resources

| Name | Type | Resource Group | Location | Environment | Status |
|------|------|-----------------|----------|-------------|--------|
| vm-lab-01-key | SSH Public Key | rg-lab-01_group | eastus | unknown | unknown |
| rg-lab-01-vnet | Virtual Network | rg-lab-01_group | eastus | unknown | unknown |
| rg-lab-01-nsg | Network Security Group | rg-lab-01_group | eastus | unknown | unknown |
| rg-lab-01-ip | Public IP Address | rg-lab-01_group | eastus | unknown | unknown |
| rg-lab-01491 | Network Interface | rg-lab-01_group | eastus | unknown | unknown |
| rg-lab-01 | Virtual Machine | rg-lab-01_group | eastus | unknown | deallocated |
| rg-lab-01_disk1_3810fafb2e9b49bd9ec24493af006a4a | Managed Disk | RG-LAB-01_GROUP | eastus | unknown | unknown |
| shutdown-computevm-rg-lab-01 | Auto-Shutdown Schedule | rg-lab-01_group | eastus | unknown | unknown |
| rg-lab-01/enablevmAccess | VM Extension | rg-lab-01_group | eastus | unknown | unknown |
| artstorageaz104 | Storage Account | rg-lab-01_group | eastus | unknown | unknown |
| vault-mqz7g0kp | Recovery Services Vault | rg-lab-01_group | eastus | unknown | unknown |
| pip-lb-01 | Public IP Address | rg-lab-01_group | eastus | unknown | unknown |
| lb-lab-01 | Load Balancer | rg-lab-01_group | eastus | unknown | unknown |
| rg-lab-01-vnet-IPv4 | Public IP Address | rg-lab-01_group | eastus | unknown | unknown |
| bastion-lab-01 | Bastion Host | rg-lab-01_group | eastus | unknown | unknown |
| bastion-lab-01-ip | Public IP Address | rg-lab-01_group | eastus | unknown | unknown |
| NetworkWatcher_eastus | Network Watcher | NetworkWatcherRG | eastus | unknown | unknown |
| vnet-final-project | Virtual Network | rg-final-project | eastus | unknown | unknown |
| nsg-final-project | Network Security Group | rg-final-project | eastus | unknown | unknown |
| vm-frontend-01_key | SSH Public Key | rg-final-project | eastus | unknown | unknown |
| vm-frontend-01-ip | Public IP Address | rg-final-project | eastus | unknown | unknown |
| vm-frontend-0155_z1 | Network Interface | rg-final-project | eastus | unknown | unknown |
| vm-frontend-01 | Virtual Machine | rg-final-project | eastus | unknown | running |
| vm-frontend-01_OsDisk_1_6dabdb3947614f64a1fa52e3e226077a | Managed Disk | RG-FINAL-PROJECT | eastus | unknown | unknown |
| law-sc200-lab01 | Log Analytics Workspace | rg-sc200-lab01 | eastus | unknown | unknown |
| SecurityInsights(law-sc200-lab01) | Monitoring Solution | rg-sc200-lab01 | eastus | unknown | unknown |

## Security Findings

- **Medium** – vm-lab-01-key: Missing required tags: owner, cost_center, environment
- **Medium** – rg-lab-01-vnet: Missing required tags: owner, cost_center, environment
- **Medium** – rg-lab-01-nsg: Missing required tags: owner, cost_center, environment
- **Medium** – rg-lab-01-ip: Missing required tags: owner, cost_center, environment
- **Medium** – rg-lab-01491: Missing required tags: owner, cost_center, environment
- **Medium** – rg-lab-01: Missing required tags: owner, cost_center, environment
- **Medium** – rg-lab-01_disk1_3810fafb2e9b49bd9ec24493af006a4a: Missing required tags: owner, cost_center, environment
- **Medium** – shutdown-computevm-rg-lab-01: Missing required tags: owner, cost_center, environment
- **Medium** – rg-lab-01/enablevmAccess: Missing required tags: owner, cost_center, environment
- **Medium** – artstorageaz104: Missing required tags: owner, cost_center, environment
- **Medium** – vault-mqz7g0kp: Missing required tags: owner, cost_center, environment
- **Medium** – pip-lb-01: Missing required tags: owner, cost_center, environment
- **Medium** – lb-lab-01: Missing required tags: owner, cost_center, environment
- **Medium** – rg-lab-01-vnet-IPv4: Missing required tags: owner, cost_center, environment
- **Medium** – bastion-lab-01: Missing required tags: owner, cost_center, environment
- **Medium** – bastion-lab-01-ip: Missing required tags: owner, cost_center, environment
- **Medium** – NetworkWatcher_eastus: Missing required tags: owner, cost_center, environment
- **Medium** – vnet-final-project: Missing required tags: owner, cost_center, environment
- **Medium** – nsg-final-project: Missing required tags: owner, cost_center, environment
- **Medium** – vm-frontend-01_key: Missing required tags: owner, cost_center, environment
- **Medium** – vm-frontend-01-ip: Missing required tags: owner, cost_center, environment
- **Medium** – vm-frontend-0155_z1: Missing required tags: owner, cost_center, environment
- **Medium** – vm-frontend-01: Missing required tags: owner, cost_center, environment
- **Medium** – vm-frontend-01_OsDisk_1_6dabdb3947614f64a1fa52e3e226077a: Missing required tags: owner, cost_center, environment
- **Medium** – law-sc200-lab01: Missing required tags: owner, cost_center, environment
- **Medium** – SecurityInsights(law-sc200-lab01): Missing required tags: owner, cost_center, environment
