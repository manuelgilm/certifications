# create the resource group
az group create --name containerized-solutions-app --location brazilsouth  
# create an environment for the container app
az containerapp env create --name containerized-solutions-env --resource-group containerized-solutions-app --location brazilsouth
# create the container app 
az containerapp create \
    --name simple-apitest \
    --resource-group containerized-solutions-app \
    --environment containerized-solutions-env \
    --image gilsama/simpleapigs:master \
    --target-port 8000 \
    --ingress 'external' \
    --query properties.configuration.ingress.fqdn