location="brazilsouth"
rg_name="cosmosdbsol"
cosmosdb_name="cosmosdbsolaccount"
# create resource group 
az group create --name $rg_name --location $location
# create cosmos db account
az cosmosdb create \
    --name $cosmosdb_name \
    --resource-group $rg_name \
    --locations regionName=$location