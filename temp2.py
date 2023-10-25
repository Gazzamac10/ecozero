import pandas as pd
import azure.functions as func
import logging
import traceback
from azure.data.tables import TableServiceClient, TableClient, UpdateMode  # Import UpdateMode from azure.data.tables
from azure.storage.blob import BlobServiceClient
import datetime
import json
import requests


# Define your Azure Table Storage connection string and table name
connection_string = "DefaultEndpointsProtocol=https;AccountName=ifcblobstorage;AccountKey=pfjYYtnqOTPPKPJFKmnPouSbb8Nxx/dA3HbQ4tlBDQepGeNEpzrwtxwFp3agDHOQjAbQV3RVLAwJ+ASt5m5Vsw==;EndpointSuffix=core.windows.net"
table_name = "ecozerostatic"

# Create a list of dictionaries from your data
data = [
    {"code": "O55", "Grid x (m)": 5, "Grid y (m)": 5, "Structural Zone (m)": 0.205, "Floor Zone (m)": 0.205},
    {"code": "O56", "Grid x (m)": 5, "Grid y (m)": 6, "Structural Zone (m)": 0.210, "Floor Zone (m)": 0.210},
    {"code": "O57", "Grid x (m)": 5, "Grid y (m)": 7, "Structural Zone (m)": 0.230, "Floor Zone (m)": 0.230},
    {"code": "O58", "Grid x (m)": 5, "Grid y (m)": 8, "Structural Zone (m)": 0.260, "Floor Zone (m)": 0.260},
    {"code": "O59", "Grid x (m)": 5, "Grid y (m)": 9, "Structural Zone (m)": 0.300, "Floor Zone (m)": 0.300}
]

try:
    # Create a TableServiceClient using the connection string
    table_service_client = TableServiceClient.from_connection_string(connection_string)

    # Check if the table exists, and if not, create it
    table_client = table_service_client.get_table_client(table_name)
    
    # Check if the table exists, and if not, create it
    table_list = table_service_client.query_tables("TableClient")
    if table_name not in table_list:
        table_service_client.create_table(table_name)

    # Insert or update each record in the table
    for record in data:
        # Upsert the entity into the table
        table_client.upsert_entity(mode=UpdateMode.MERGE, entity=record)

    print("Data uploaded to Azure Table Storage successfully")

except Exception as error:
    print("Error uploading data to Azure Table Storage:", error)