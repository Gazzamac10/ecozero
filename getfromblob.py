from azure.data.tables import TableServiceClient

# Define your connection string and table name
connection_string = "DefaultEndpointsProtocol=https;AccountName=ifcblobstorage;AccountKey=pfjYYtnqOTPPKPJFKmnPouSbb8Nxx/dA3HbQ4tlBDQepGeNEpzrwtxwFp3agDHOQjAbQV3RVLAwJ+ASt5m5Vsw==;EndpointSuffix=core.windows.net"
table_name = "ecozerostatic"

# Create a TableServiceClient using the connection string
table_service_client = TableServiceClient.from_connection_string(connection_string)

# Get a reference to the table (no need to create it if it already exists)
table_client = table_service_client.get_table_client(table_name)

# Define an empty query to retrieve all entities
query = None

# Execute the query to retrieve all entities
entities = table_client.query_entities(query)

# Iterate through the retrieved entities
for entity in entities:
    # Access and process entity properties (columns) for each entity
    partition_key = entity['PartitionKey']
    row_key = entity['RowKey']
    
    # Iterate through the properties of the entity to access all columns
    for property_name, property_value in entity.items():
        print(f"{property_name}: {property_value}")

    # Print additional information if needed
    print(f"PartitionKey: {partition_key}, RowKey: {row_key}")
