from azure.cosmos import CosmosClient 
from azure.cosmos import PartitionKey 
from typing import Dict 
from typing import Any 
import os 
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

client = CosmosClient(
    os.getenv("ACCOUNT_URI"),   
    os.getenv("ACCOUNT_KEY")
)

# start create a database 
db_name = "cosmosdbsol"
try:
    database = client.create_database(id=db_name)
except Exception as e:
    print(f"Database '{db_name}' already exists. Using existing database.")
    database = client.get_database_client(db_name)

# end create a database
    
# start create a container
container_name = "products"
try:
    container = database.create_container(id=container_name, partition_key=PartitionKey(path="/productName"))
except Exception as e:
    print(f"Container '{container_name}' already exists. Using existing container.")
    container = database.get_container_client(container_name)

# end create a container

# start get container 
database = client.get_database_client(db_name)
container = database.get_container_client(container_name)
# end get container

# start list containers 
database = client.get_database_client(db_name)
for contanier_dict in database.list_containers():
    print(f"Container ID: {contanier_dict['id']}")

# start insert item
container = database.get_container_client(container_name)
for i in range(1,10):
    item = {
        "id": f"item-{i}",
        "productName": "Widget",
        "productModel":"Model {}".format(i),
    }
    container.upsert_item(item)

# end insert item

# start modify item
item = container.read_item(item="item-2", partition_key="Widget")
item["productModel"] = "DISCONTINUED"
updated_item = container.upsert_item(item)
# end modify item

# [START query_items]
import json

for queried_item in container.query_items(
    query='SELECT * FROM products p WHERE p.productModel <> "DISCONTINUED"',
    enable_cross_partition_query=True,
):
    print(json.dumps(queried_item, indent=True))
# [END query_items]
