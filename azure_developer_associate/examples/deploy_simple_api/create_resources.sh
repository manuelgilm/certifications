# create resource group for the Simple API deployment
az group create --name SimpleApiRG --location brazilsouth
# create service plan for the simple API
az appservice plan create --name SimpleApiPlan --resource-group SimpleApiRG --sku S1 --is-linux
# create web app for the simple API 
az webapp create --name simpleapigs --resource-group SimpleApiRG --plan SimpleApiPlan --basic-auth Enabled --runtime "Python:3.12" 