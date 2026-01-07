# create resource groupo 
az group create --name containerized-solutions --location brazilsouth 

DNS_NAME_LABEL=aci-example-$RANDOM
# create a container instance
az container create --resource-group containerized-solutions \
    --name simpleapigs \
    --image gilsama/simpleapigs:master \
    --ports 80 \
    --dns-name-label $DNS_NAME_LABEL --location brazilsouth \
    --os-type Linux \
    --cpu 1 \
    --memory 1.5 \
    --registry-password <passord>
    --registry-username <username>

az container show --resource-group containerized-solutions \
    --name simpleapigs \
    --query "{FQDN:ipAddress.fqdn,ProvisioningState:provisioningState}" \
    --out table     

# restart policy
az container create --resource-group <resource group name> \
    --name <container name> \
    --image <image name> \
    --restart-policy OnFailure

# Available policies:
# - Always: Containers in the container group are always restarted. This is the default setting applied when no restart policy is specified at container creation.
# - OnFailure: Containers in the container group are restarted only if they exit with a non-zero exit code.
# - Never: Containers in the container group are never restarted, regardless of their exit code.  The containers run at most once.