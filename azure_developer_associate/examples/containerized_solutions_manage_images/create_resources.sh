# create resource group 
az group create --name "containerized-solutions-rg" --location "brazilsouth"
# create and azure container registry
az acr create --resource-group "containerized-solutions-rg" --name "containersolutionsacr" --sku "Basic"
# build and push the image to the registry
az acr build --image sample/hello-world:v1 --registry containersolutionsacr --file Dockerfile .
# list the repositories in the registry
az acr repository list --name containersolutionsacr --output table
# listing tags
az acr repository show-tags --name containersolutionsacr --repository sample/hello-world --output table
# running the image
az acr run --registry containersolutionsacr --cmd '$Registry/sample/hello-world:v1' /dev/null
