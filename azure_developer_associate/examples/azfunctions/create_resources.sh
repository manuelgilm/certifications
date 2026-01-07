# Create a resource group for Azure Functions
echo "Creating resource group for Azure Functions..."
az group create --name azfunctions --location brazilsouth 

#Create an Azure storage account in the resource group
echo "Creating storage account for Azure Functions..."
az storage account create --name azfunctionsstoragegs --location brazilsouth --resource-group azfunctions --sku Standard_LRS
# Create an Azure Functions app in the resource group
echo "Creating Azure Functions app..."
az functionapp create --name azfunctionsappgs$RANDOM \
    --storage-account azfunctionsstoragegs \
    --consumption-plan-location brazilsouth \
    --resource-group azfunctions \
    --functions-version "4" 
