from azure.identity import DefaultAzureCredential
from azure.mgmt.resource.resources import ResourceManagementClient
from azure.mgmt.compute import ComputeManagementClient

RESOURCE_TYPE_LABELS = {
    "Microsoft.Compute/virtualMachines": "Virtual Machine",
    "Microsoft.Compute/disks": "Managed Disk",
    "Microsoft.Compute/sshPublicKeys": "SSH Public Key",
    "Microsoft.Compute/virtualMachines/extensions": "VM Extension",
    "Microsoft.Network/virtualNetworks": "Virtual Network",
    "Microsoft.Network/networkSecurityGroups": "Network Security Group",
    "Microsoft.Network/publicIPAddresses": "Public IP Address",
    "Microsoft.Network/networkInterfaces": "Network Interface",
    "Microsoft.Network/loadBalancers": "Load Balancer",
    "Microsoft.Network/bastionHosts": "Bastion Host",
    "Microsoft.Network/networkWatchers": "Network Watcher",
    "Microsoft.Storage/storageAccounts": "Storage Account",
    "Microsoft.KeyVault/vaults": "Key Vault",
    "Microsoft.Sql/servers": "SQL Server",
    "Microsoft.Sql/servers/databases": "SQL Database",
    "Microsoft.RecoveryServices/vaults": "Recovery Services Vault",
    "Microsoft.DevTestLab/schedules": "Auto-Shutdown Schedule",
    "Microsoft.OperationalInsights/workspaces": "Log Analytics Workspace",
    "Microsoft.OperationsManagement/solutions": "Monitoring Solution",
}


def get_resource_type_label(resource_type):
    return RESOURCE_TYPE_LABELS.get(resource_type, resource_type.split("/")[-1])


def get_vm_power_state(compute_client, resource_group, vm_name):
    try:
        instance_view = compute_client.virtual_machines.instance_view(resource_group, vm_name)
    except Exception:
        return "unknown"

    for status in instance_view.statuses:
        if status.code.startswith("PowerState/"):
            return status.code.split("/")[-1]

    return "unknown"


def fetch_live_resources(subscription_id):
    credential = DefaultAzureCredential()
    resource_client = ResourceManagementClient(credential, subscription_id)
    compute_client = ComputeManagementClient(credential, subscription_id)

    resources = []

    for resource in resource_client.resources.list():
        tags = resource.tags or {}
        resource_group = resource.id.split("/")[4]

        status = "unknown"
        if resource.type == "Microsoft.Compute/virtualMachines":
            status = get_vm_power_state(compute_client, resource_group, resource.name)

        resources.append({
            "name": resource.name,
            "resource_type": get_resource_type_label(resource.type),
            "resource_group": resource_group,
            "location": resource.location,
            "subscription": subscription_id,
            "environment": tags.get("environment", "unknown"),
            "status": status,
            "tags": tags,
        })

    return resources
