import pandas as pd
from azure.data.tables import TableServiceClient


connection_string = "DefaultEndpointsProtocol=https;AccountName=ifcblobstorage;AccountKey=pfjYYtnqOTPPKPJFKmnPouSbb8Nxx/dA3HbQ4tlBDQepGeNEpzrwtxwFp3agDHOQjAbQV3RVLAwJ+ASt5m5Vsw==;EndpointSuffix=core.windows.net"
table_name = "ecozerostatic"


# Create a TableServiceClient using the connection string
table_service_client = TableServiceClient.from_connection_string(connection_string)

# Get a reference to the table (no need to create it if it already exists)
table_client = table_service_client.get_table_client(table_name)
    

def get_all_column_headers():
    # Initialize a TableServiceClient
    # Get the table's entity schema, which contains column names
    out = []
    entity_schema = table_client.list_entities()
    for item in entity_schema:
        out = item.keys()
    return out


def query_blob_table_to_dataframe(column_names):
    # Define a query to retrieve specific columns
    query = None  # You can add conditions if needed

    # Execute the query to retrieve entities with the specified columns
    entities = table_client.query_entities(query, select=column_names)

    # Create a list of dictionaries to hold the results
    result_data = []

    # Iterate through the retrieved entities
    for entity in entities:
        row_data = {}
        for column_name in column_names:
            row_data[column_name] = entity.get(column_name, None)
        result_data.append(row_data)

    # Create a Pandas DataFrame from the result data
    dataframe = pd.DataFrame(result_data)

    return dataframe

# Example usage:
#selected_columns = ["code","Gridxm","Gridym"]  # Replace with your desired column names
#selected_columns = get_all_column_headers() # Replace with your desired column names
#result_dataframe = query_blob_table_to_dataframe(selected_columns)

# Now, you can work with the 'result_dataframe' as a Pandas DataFrame
#print(result_dataframe.columns.tolist())
#print(result_dataframe[['code','Gridxm']])

#save_list_to_txt('ecocolunms.txt',result_dataframe.columns.tolist())
