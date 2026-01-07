from azure.identity import DefaultAzureCredential
from azure.mgmt.storage import StorageManagementClient
from azure.mgmt.resource import ResourceManagementClient

from typing import Optional
from dotenv import load_dotenv
import os


def get_resource_client(subscription_id: Optional[str] = None):
    """
    Get the Azure Resource Management client.

    :param subscription_id: Azure Subscription ID. If None, it will be read from the environment variable 'AZURE_SUBSCRIPTION_ID'.
    :return: ResourceManagementClient instance.
    """
    if subscription_id is None:
        subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")
        if subscription_id is None:
            raise ValueError(
                "Subscription ID must be provided or set in the environment variable 'AZURE_SUBSCRIPTION_ID'."
            )
    credential = DefaultAzureCredential()
    resource_client = ResourceManagementClient(credential, subscription_id)
    return resource_client


def get_storage_client(subscription_id: Optional[str] = None):
    """
    Get the Azure Storage Management client.

    :param subscription_id: Azure Subscription ID. If None, it will be read from the environment variable 'AZURE_SUBSCRIPTION_ID'.
    :return: StorageManagementClient instance.
    """
    if subscription_id is None:
        subscription_id = os.getenv("AZURE_SUBSCRIPTION_ID")
        if subscription_id is None:
            raise ValueError(
                "Subscription ID must be provided or set in the environment variable 'AZURE_SUBSCRIPTION_ID'."
            )
    credential = DefaultAzureCredential()
    storage_client = StorageManagementClient(credential, subscription_id)
    return storage_client


def create_resource_group(
    group_name: str, location: str, resource_client: ResourceManagementClient
) -> Optional[object]:
    """
    Create a resource group in the specified location.

    :param group_name: Name of the resource group.
    :param location: Azure region where the resource group will be created.
    :param resource_client: An instance of ResourceManagementClient.
    :return: The created resource group.
    """
    resource_group_params = {"location": location}
    group_names = [rg.name for rg in resource_client.resource_groups.list()]
    if group_name in group_names:
        print(f"Resource Group '{group_name}' already exists.")
        return None
    resource_group = resource_client.resource_groups.create_or_update(
        group_name, resource_group_params
    )
    return resource_group


def create_storage_account(
    group_name: str,
    storage_account_name: str,
    location: str,
    storage_client: StorageManagementClient,
) -> Optional[object]:
    """
    Create a storage account in the specified resource group and location.

    :param group_name: Name of the resource group.
    :param storage_account_name: Name of the storage account. Must be globally unique.
    :param location: Azure region where the storage account will be created.
    :param storage_client: An instance of StorageManagementClient.
    :return: The created storage account.
    """
    strg_names = [strg.name for strg in storage_client.storage_accounts.list()]
    if storage_account_name in strg_names:
        print(f"Storage Account '{storage_account_name}' already exists.")
        return None
    strg_result = storage_client.storage_accounts.begin_create(
        group_name,
        storage_account_name,
        {
            "sku": {"name": "Standard_LRS"},
            "kind": "StorageV2",
            "location": location,
            "encryption": {
                "services": {
                    "file": {"key_type": "Account", "enabled": True},
                    "blob": {"key_type": "Account", "enabled": True},
                },
                "key_source": "Microsoft.Storage",
            },
            "tags": {"key1": "value1", "key2": "value2"},
        },
    ).result()
    return strg_result


def create_blob_container(
    group_name: str, storage_account_name: str, container_name: str, storage_client: StorageManagementClient
) -> Optional[object]:
    """
    Create a blob container in the specified storage account.

    :param group_name: Name of the resource group.
    :param storage_account_name: Name of the storage account.
    :param container_name: Name of the blob container.
    :param storage_client: An instance of StorageManagementClient.
    :return: The created blob container.
    """
    containers = storage_client.blob_containers.list(group_name, storage_account_name)
    if container_name in [container.name for container in containers]:
        print(f"Blob Container '{container_name}' already exists.")
        return None
    container = storage_client.blob_containers.create(
        group_name, storage_account_name, container_name, {}
    )
    print(f"Blob Container '{container_name}' created.")
    return container

def clean(resource_client: ResourceManagementClient, group_name: str):
    """
    Delete the specified resource group and all its resources.

    :param resource_client: An instance of ResourceManagementClient.
    :param group_name: Name of the resource group to delete.
    """
    print(f"Deleting Resource Group: {group_name}")
    delete_async_operation = resource_client.resource_groups.begin_delete(group_name)
    delete_async_operation.wait()
    print(f"Resource Group '{group_name}' deleted.")

def main(resource_client: Optional[ResourceManagementClient] = None, storage_client: Optional[StorageManagementClient] = None):

    # creating resource group
    create_resource_group(GROUP_NAME, LOCATION, resource_client)

    # creating storage account
    create_storage_account(GROUP_NAME, STORAGE_ACCOUNT_NAME, LOCATION, storage_client)

    # creating a blob container
    create_blob_container(GROUP_NAME, STORAGE_ACCOUNT_NAME, CONTAINER_NAME, storage_client)


if __name__ == "__main__":
    import sys
    load_dotenv()
    GROUP_NAME = "storageaccountgs"
    STORAGE_ACCOUNT_NAME = "mystorageaccountgs12345"
    CONTAINER_NAME = "mycontainer"
    LOCATION = "brazilsouth"

    resource_client = get_resource_client()
    storage_client = get_storage_client()
    
    args = sys.argv[1:]
    if args and args[0] == "run":
        main(resource_client, storage_client)
    elif args and args[0] == "clean":
        clean(resource_client, GROUP_NAME)
    else:
        print("Pass 'run' as an argument to execute the main function.")
