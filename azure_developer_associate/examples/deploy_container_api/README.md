# Deploy Simple Container API Example

This example implements the following diagram.

![alt text](image-2.png)

## Creating pipeline to build and publish the image to DockerHub

To create the image we are using the Workflow defined in `.github\workflows\master_container_simple_api.yml` which uses the action `docker/build-push-action@3b5e8027fcad23fda98b2e3ac259d8d67585f671` to build and push the image.

## Creating resources. 

The `create_resources.sh` script automates the creation of the resource group, service plan, and web app. There are some settings that the command does not update.

**Creating a resource group**

```bash
az group create --name SimpleApiRG --location brazilsouth
```

**Creating the service plan**
```bash
az appservice plan create --name SimpleApiPlan --resource-group SimpleApiRG --sku S1 --is-linux
```

**Creating the webapp**

```bash
az webapp create \
    --name simpleapicontainer \
    --resource-group SimpleApiRG \
    --plan SimpleApiPlan \
    --container-image-name <repository/image-name:tag> \
    --container-registry-user <username> \
    --container-registry-password <password>
```

![alt text](image.png)

* Registry Source: The registry from which the image will be pulled. 
* Repository Access: This enables credentials to access the Registry
    * Login: The username
    * Password: Password.

* Full Image Name and Tag: Image name in format `<namespace>/<image-name>:tag`

## Results
In the browser we can see the following:

![alt text](image-1.png)