# Deploy Simple API Example

## Creating resources. 
The `create_resources.sh` script automates the creation of the resource group, service plan, and web app. Note that connecting the web app to the GitHub repository must be performed manually.

**create resource group for the Simple API deployment**
```bash
az group create --name SimpleApiRG --location brazilsouth
```

**create service plan for the simple API**

```bash
az appservice plan create --name SimpleApiPlan --resource-group SimpleApiRG --sku S1 --is-linux
```

**create web app for the simple API** 
```bash
az webapp create --name simpleapigs --resource-group SimpleApiRG --plan SimpleApiPlan --basic-auth Enabled --runtime "Python:3.12" 
```
## Configuring Repository

* Choose GitHub 

* Github Configurations:
    * Choose the right organization (where you have the repository)
    * Choose the right repository (where you have the code)
    * Choose the branch. (where you have the code)
    * Workflow option: 
        * Overwrite the workflow (only if a workflow was created before)
        * Use existing workflow. 

    ![alt text](image-3.png)

* Authentication Settings
   * Authentication type:
        * User-asssigned identity
        * Basic Authentication (Using this one)

        ![alt text](image-4.png)

    * Click on **save**


## Configuring the Actions to use poetry.

![alt text](image-5.png)

Comment that tasks that are not needed because we are using poetry in the setup command. Commit and push this will run the workflow.


## Configuring the setup command

Ensure that the **Setup Command** field is configured accurately. An incorrect setup command may prevent the application from starting as expected.

![alt text](image.png)

The command is: 
```bash
pip install poetry && \
cd examples/deploy_simple_api/simpleapi && \
poetry install && \
poetry run fastapi dev simpleapi --port 8000 --host 0.0.0.0
```

**Results**

In **Overview -> Properties -> Domains -> Default Domain** Click the link created by azure, this will be the url of the API. Add `/docs` to access fastAPI docs. For instance `https://simpleapigs.azurewebsites.net/docs`

In the browser we can see the following:
![alt text](image-1.png)
