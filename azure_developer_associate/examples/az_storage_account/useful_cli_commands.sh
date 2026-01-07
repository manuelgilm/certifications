rg_name="storageaccountdemogs"
storage_account_name="storageaccountdemogs"
location="brazilsouth"
container_name="testcontainer"
# create resource group 
az group create --name $rg_name --location $location

# create storage account 
az storage account create --name $storage_account_name --resource-group $rg_name --location $location --sku Standard_LRS

# set lifecycle management policy to move blobs to cool tier after 1 day
az storage account management-policy create --account-name $storage_account_name --policy @policy.json --resource-group $rg_name

# create a container within the storage account
az storage container create --name $container_name --account-name $storage_account_name

# upload readme file to the container
az storage blob upload --account-name $storage_account_name --container-name $container_name --file README.md --name test
