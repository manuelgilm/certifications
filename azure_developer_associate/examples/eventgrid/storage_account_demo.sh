topic_name=eventgridgstopic
rg_name=eventgridgs
location=brazilsouth
storage_account_name=eventgridgsstorage
storage_container_name=testcontainer
function_app_name=eventgridgsfunctionapp
service_plan_name=eventgridgsserviceplan

# create resource group.
az group create --name $rg_name --location $location

# create a storage account
az storage account create --name $storage_account_name --resource-group $rg_name --location $location --sku Standard_LRS

# create a container within the storage account
az storage container create --name $storage_container_name --account-name $storage_account_name

# create service plan
az appservice plan create --name $service_plan_name --resource-group $rg_name --sku S1 --is-linux

# create function app
az functionapp create \
    --name $function_app_name \
    --storage-account $storage_account_name \
    --plan $service_plan_name \
    --resource-group $rg_name \
    --runtime python \
    --runtime-version 3.12 \


# create local function
func new \
    --name $function_app_name \
    --language python \
    --template eventgrid_trigger \
    --worker-runtime python \

# publish local function
func azure functionapp publish $function_app_name

