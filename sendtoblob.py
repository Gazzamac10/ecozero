import pandas as pd
import azure.functions as func
import logging
import traceback
from azure.data.tables import TableServiceClient, TableClient, UpdateMode  # Import UpdateMode from azure.data.tables
from azure.storage.blob import BlobServiceClient
import datetime
import json
import requests


def readtext(path):
    # Initialize an empty list to store the lines from the file
    lines = []

    # Open the 'headers.txt' file for reading
    with open(path, 'r') as file:
        for line in file:
            # Append each line (as a string) to the list
            lines.append(line.strip())
    return lines


def save_list_to_txt(filename, input_list):
    try:
        with open(filename, 'w') as file:
            for item in input_list:
                file.write(str(item) + '\n')
        print(f"List saved to {filename}")
    except IOError:
        print("An error occurred while saving the list to the file.")
        
        
connection_string = "DefaultEndpointsProtocol=https;AccountName=ifcblobstorage;AccountKey=pfjYYtnqOTPPKPJFKmnPouSbb8Nxx/dA3HbQ4tlBDQepGeNEpzrwtxwFp3agDHOQjAbQV3RVLAwJ+ASt5m5Vsw==;EndpointSuffix=core.windows.net"
table_name = "ecozerostatic"

excel_file_path = 'eco1000.xlsx'
df = pd.read_excel(excel_file_path)
df = df.astype(str)

new = readtext('new.txt')

df.columns = new


def replace_column_names(df, old_chars, new_chars):
    df.columns = [col.replace(old_chars, new_chars) for col in df.columns]

replace_column_names(df,'(','')
replace_column_names(df,')','')
replace_column_names(df,' ','')
replace_column_names(df,'-','_')
replace_column_names(df,'/','_')
replace_column_names(df,',','_')
replace_column_names(df,'.','_')
replace_column_names(df,"'",'_')
replace_column_names(df,"\n",'_')


#df = df.iloc[:1, :5]

row_dicts = df.to_dict(orient='records')
list = row_dicts

rk = df['code'].tolist()

#save_list_to_txt('newheaders.txt',df.columns)

# Create a TableServiceClient using the connection string
table_service_client = TableServiceClient.from_connection_string(connection_string)

# Get a reference to the table (no need to create it if it already exists)
table_client = table_service_client.get_table_client(table_name)

def createrow(r,rkey):
    try:
        # Define a PartitionKey
        partition_key = "ecozerostatic"  # Replace with an appropriate value
        #row_key = f"{partition_key}_{str(datetime.datetime.now())}"
        row_key = rkey
        
        r.update({"PartitionKey": partition_key, "RowKey": row_key})
        table_client.upsert_entity(mode=UpdateMode.MERGE, entity=r)
        #print (r)
    except Exception as error:
        logging.warning("Error uploading data to Azure Table Storage: {0}".format(error))
        logging.warning(traceback.format_exc())


#[createrow(list[i],rk[i])for i in range(len(list))]
