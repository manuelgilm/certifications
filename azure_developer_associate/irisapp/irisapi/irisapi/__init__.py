from fastapi import FastAPI 
from fastapi.responses import JSONResponse
from irisapi.utils.dummy import get_random_prediction
from contextlib import asynccontextmanager
import os 
from azure.cosmos import CosmosClient 
from azure.cosmos import PartitionKey 
import random

version="0.1.0"
description="Iris API for Cosmos DB"
storage = {}
@asynccontextmanager
async def lifespan(app: FastAPI) -> FastAPI:
    """
    Lifespan event handler for FastAPI.
    """
    
    cosmos_db_uri = os.getenv("COSMOSDB_URI")
    cosmos_db_primary_key = os.getenv("COSMOSDB_PRIMARY_KEY")
    if not cosmos_db_uri or not cosmos_db_primary_key:
        raise ValueError("COSMOSDB_URI and COSMOSDB_PRIMARY_KEY environment variables must be set.")
    # Initialize Cosmos DB client or any other setup can be done here
    client = CosmosClient(
        cosmos_db_uri,   
        cosmos_db_primary_key
    )

    create_database = "irisappdb"
    try:
        database = client.create_database(id=create_database)
    except Exception as e:
        print(f"Database '{create_database}' already exists. Using existing database.")
        database = client.get_database_client(create_database)

    create_container = "irisapppredictions"
    try:
        container = database.create_container(id=create_container, partition_key=PartitionKey(path="/prediction"))
    except Exception as e:
        print(f"Container '{create_container}' already exists. Using existing container.")
        container = database.get_container_client(create_container)
    storage['client'] = client
    storage['database'] = database
    storage['container'] = container
    yield
    # Clear the storage dictionary
    storage.clear()
    
app = FastAPI(lifespan=lifespan)



@app.get("/")
async def read_root():
    return {"message": "Welcome to the Iris API", "version": version, "description": description}

@app.post("/predict")
async def predict(data: dict)-> JSONResponse:
    """
    Predict the class of iris flowers based on input features.
    """
    # Here you would typically call your model to make a prediction
    # For now, we will return a mock response
    prediction = get_random_prediction()
    # Store the prediction in Cosmos DB
    container = storage['container']
    prediction = {
        "id": str(random.randint(0,1000)),
        "confidence": prediction["confidence"],
        "prediction": prediction["prediction"]
    }
    try:
        container.upsert_item(prediction)
    except Exception as e:
        print(f"Error inserting item into Cosmos DB: {e}")
        return JSONResponse(content={"error": "Failed to insert prediction into Cosmos DB"})
    # Return the prediction as a JSON response
    return JSONResponse(content=prediction)

