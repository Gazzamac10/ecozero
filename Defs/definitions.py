from azure.data.tables import TableServiceClient
from azure.core.exceptions import HttpResponseError
import pandas as pd



def factoredLoads(df,gk,qk,storeys):
    df['CornerNed'] = (gk * df['CornerColumn_Gk_kN'] + qk * df['CornerColumn_Qk_kN']) * storeys
    df['EdgeNed'] = (gk * df['EdgeColumn_Gk_kN'] + qk * df['EdgeColumn_Qk_kN']) * storeys
    df['InternalNed'] = (gk * df['InternalColumn_Gk_kN'] + qk * df['InternalColumn_Qk_kN']) * storeys
    columnLoads_to_keep = ['CornerNed', 'EdgeNed', 'InternalNed']
    df = df[columnLoads_to_keep]
    return df

def query_blob_table(table_name, connection_string, partitionKey, column, columnValue):
    query = f"PartitionKey eq '{partitionKey}' and {column} eq '{columnValue}'"

    try:
        # Create a TableServiceClient using the connection string
        table_service_client = TableServiceClient.from_connection_string(connection_string)

        # Get a reference to the table (no need to create it if it already exists)
        table_client = table_service_client.get_table_client(table_name)

        # Execute the query to retrieve entities with all columns
        entities = list(table_client.query_entities(query))  # Convert to a list

        return entities
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        return []


def get_value_from_entities(entities, key):
    for entity in entities:
        if key in entity:
            return entity[key]
    return None


def get_entity_keys(entities):
    key_names = set()  # Using a set to ensure unique key names

    for entity in entities:
        key_names.update(entity.keys())

    return list(key_names)


def query_azure_table_to_dataframe(connection_string, table_name):
    try:
        # Create a TableServiceClient using the connection string
        service_client = TableServiceClient.from_connection_string(connection_string)

        # Get a reference to the table
        table_client = service_client.get_table_client(table_name)

        # Query the table and retrieve results as a list of dictionaries
        entities = list(table_client.list_entities())

        # Convert the list of entities to a DataFrame
        df = pd.DataFrame(entities)

        return df

    except HttpResponseError as e:
        print(f"Error: {e}")
        return None


def ColumnNumbers(bayX,bayY):
    columnCorners = 4
    columnEdges = ((bayX-1)*(bayY-1))-columnCorners
    columnsInternal = (bayX*bayY)-columnCorners-columnEdges
    return columnsInternal,columnCorners,columnEdges

def floorArea(bayX,bayY,gridX,gridY):
    floor = (gridX*bayX)*(gridY*bayY)
    return floor