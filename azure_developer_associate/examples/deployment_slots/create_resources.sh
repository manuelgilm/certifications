#create resource group 
az group create --name "deployment-slots-rg" --location "brazilsouth"
# create app service plan 
az appservice plan create --name "deployment-slots-sp" --resource-group "deployment-slots-rg" --sku "S1" --is-linux # slots are only available in Standard and Premium plans
# create web app
az webapp create --name "depsloptsapp" --resource-group "deployment-slots-rg" --plan "deployment-slots-sp"
# create staging slot 
az webapp deployment slot create 
--name "depsloptsapp" 
--resource-group "deployment-slots-rg" 
--slot "staging" 
--configuration-source "depsloptsapp" 
--container-image-name gilsama/simpleapigs:latest 
--container-registry-password <password>
--container-registry-user <username>
--container-image-name "gilsama/simpleapigs:staging"
