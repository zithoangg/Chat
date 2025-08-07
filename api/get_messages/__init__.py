import azure.functions as func
import logging
import os
import json
import uuid
from azure.cosmos import CosmosClient, exceptions

# Initialize Cosmos DB client
cosmos_client = CosmosClient(os.environ["COSMOS_ENDPOINT"], os.environ["COSMOS_KEY"])
database = cosmos_client.get_database_client(os.environ["COSMOS_DB_NAME"])
container = database.get_container_client(os.environ["COSMOS_CONTAINER_NAME"])

def main(req: func.HttpRequest) -> func.HttpResponse:
    try:
        # Get message from the request body
        req_body = req.get_json()
        message = req_body.get("message")
        
        if message:
            # Store the message in Cosmos DB
            item = {
                "id": str(uuid.uuid4()),  # Generate a unique ID for each message
                "message": message
            }
            container.create_item(body=item)  # Insert the message into Cosmos DB
            return func.HttpResponse(f"Message '{message}' saved successfully!", status_code=200)
        else:
            return func.HttpResponse("No message provided", status_code=400)
    
    except exceptions.CosmosResourceNotFoundError as e:
        logging.error(f"Error storing message: {e}")
        return func.HttpResponse("Failed to store message", status_code=500)
