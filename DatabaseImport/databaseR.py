import warnings
import pandas as pd
from azure.data.tables import TableServiceClient
import InputR
from Defs import definitions

# Suppress FutureWarnings
warnings.simplefilter(action='ignore', category=FutureWarning)

gridXdb = min(InputR.gridX,InputR.gridY)
gridYdb = max(InputR.gridX,InputR.gridY)
buildingUseDb = InputR.building_use
#print(gridXdb, gridYdb, buildingUseDb)

#Code for Database Selection
databaseCode = buildingUseDb[0] + str(gridXdb)+str(gridYdb)

corner = InputR.columnCorners
edge = InputR.columnEdges
internal = InputR.columnsInternal

storeys = InputR.storeys
storeyHeight = InputR.floorToCeiling
facadeType = InputR.facadeType

#Loading Schedule
##connect to the static data in blob
searchvalue = InputR.facadeType
# Connection string and table name
connection_string = "DefaultEndpointsProtocol=https;AccountName=ifcblobstorage;AccountKey=pfjYYtnqOTPPKPJFKmnPouSbb8Nxx/dA3HbQ4tlBDQepGeNEpzrwtxwFp3agDHOQjAbQV3RVLAwJ+ASt5m5Vsw==;EndpointSuffix=core.windows.net"
table_name = "LoadingFacade"

facadeTable = "LoadingFacade"
floorLoadTable = "LoadingFloorPlate"
floorFinishesServiceZoneTable = "FloorFinishesServiceZone"

facadeType = InputR.facadeType

def get_value_by_description(searchvalue,tableName,connectionstring):
    # Create a filter condition to match the "Description" column with searchvalue
    filter_condition = f"Description eq '{searchvalue}'"
    
        # Create a TableServiceClient using the connection string
    table_service_client = TableServiceClient.from_connection_string(connectionstring)

    # Get a reference to the table (no need to create it if it already exists)
    table_client = table_service_client.get_table_client(tableName)

    # Define a query with the filter condition to retrieve the specific column
    query = filter_condition

    # Execute the query to retrieve the entity with the specified column
    entity = next(table_client.query_entities(query), None)

    # Get the value from "gk__kN_m2_" or return None if not found
    result_value = entity.get("gk__kN_m2_", None) if entity is not None else None

    return result_value

#Outputs
facadeLoad = (float(get_value_by_description(facadeType,facadeTable,connection_string))*InputR.floorToCeiling)
if(facadeLoad<10):
    facadeLoadRC = 0
else:
    facadeLoadRC = facadeLoad-10
    
#print("Value for ", facadeType, ":", facadeLoad)
#print("FacadeLoad for RC is ", facadeLoadRC)



# Now we need to load in the database and return row values for each match to the databasecode
tableName = 'ecozerostatic'
column = 'RowKey'
connString = connection_string
#RC Flat Slab Values
# use the look up def in the loading schedule sheet to get each type as a row
DBselectRow = definitions.query_blob_table(tableName,connString,tableName,column,databaseCode)


#Build the summary table as a dataframe for operating
# Suppress FutureWarnings
warnings.simplefilter(action='ignore', category=FutureWarning)
df = pd.DataFrame(DBselectRow)


# The list of row names, needs to match the column names, will break if column names are renamed in Azure
new_row_names = [
    'CLTGlulamandSteelColumnHybrid',
    'CompositeCellBeamswithMetalDecking',
    'CompositeRolledSteelwithMetalDecking',
    'Non_CompositeRolledSteelwithPCCPlanks',
    'One_WaySpanningRC',
    'PTRCFlatSlab',
    'PrecastHollowcorewithIn_situRCBeams',
    'RCFlatSlab',
    'RCRibSlab',
    'SteelFramewithCLTSlabs',
    'Two_wayRCSlab'
]

# Create a the summary DataFrame with the new row names
summary_df = pd.DataFrame(index=new_row_names)

# Iterate through the columns of the original DataFrame
for col in df.columns:
    # Check if the column contains any of the new row names
    matching_row_name = next((row_name for row_name in new_row_names if row_name in col), None)
    if matching_row_name is not None:
        # Extract the value from the original DataFrame
        value = df.at[0, col]
        # If the value is NaN or 'nan', replace it with '0'
        if pd.isna(value) or value == 'nan':
            value = '0'
        else:
            # Convert the value to a string
            value = str(value)
        # Add it to the new DataFrame
        summary_df.at[matching_row_name, col.replace(matching_row_name + '_', '')] = value

#convert any number values to float and round to three
for row in summary_df.index:
    for col in summary_df.columns:
        value = summary_df.at[row, col]
        try:
            numeric_value = float(value)
            summary_df.at[row, col] = round(numeric_value, 3)
        except (ValueError, TypeError):
            pass
        
#Adjust the columns to suit the summary order and to include the various factors, adjustments and alterations required. 

# for RC columns take the Qk value as calculated in the database from the steel options.
#This should be queried
# Check if 'RC' is present in any part of every row's index
rc_rows = [row for row in summary_df.index if 'RC' in row]

if rc_rows:
    # Get the corresponding values from the 'SteelFramewithCLTSlabs' row
    steel_fram_values = summary_df.loc['SteelFramewithCLTSlabs', ['InternalColumn_Qk_kN', 'EdgeColumn_Qk_kN']]

    # Update the 'InternalColumn_Qk_kN' and 'EdgeColumn_Qk_kN' columns for 'RC' rows
    summary_df.loc[rc_rows, ['InternalColumn_Qk_kN', 'EdgeColumn_Qk_kN']] = steel_fram_values.values


#Adjust the edge and corner columns to include facade loading
# Iterate through the rows of the summary DataFrame
for row in summary_df.index:
    structural_zone = summary_df.at[row, 'StructuralZonem']
    
    if 'RC' in row:
        # Use facadeLoadRC when "RC" is present in the row name
        facade_load = facadeLoadRC
    else:
        # Use facadeLoad for other rows
        facade_load = facadeLoad
    
    if structural_zone == 0:
        # If StructuralZonem is 0, set EdgeColumn_Gk_kN and CornerColumn_Gk_kN to 0
        summary_df.at[row, 'EdgeColumn_Gk_kN'] = 0
        summary_df.at[row, 'CornerColumn_Gk_kN'] = 0
    else:
        # Calculate the new values for EdgeColumn_Gk_kN and CornerColumn_Gk_kN
        old_edge_gk = float(summary_df.at[row, 'EdgeColumn_Gk_kN'])
        old_corner_gk = float(summary_df.at[row, 'CornerColumn_Gk_kN'])
        
        new_edge_gk = old_edge_gk + (max(int(gridXdb), int(gridYdb))) * facade_load
        new_corner_gk = old_corner_gk + 0.5 * (int(gridXdb) + int(gridYdb)) * facade_load
        
        # Update the EdgeColumn_Gk_kN and CornerColumn_Gk_kN columns
        summary_df.at[row, 'EdgeColumn_Gk_kN'] = new_edge_gk
        summary_df.at[row, 'CornerColumn_Gk_kN'] = new_corner_gk

#increase steelwork kg/m2 by 10% 
# Iterate through the rows of the summary DataFrame
for row in summary_df.index:
    if 'RC' in row:
        # If "RC" is present in the row name, set Steelworkkg_m2 as is
        summary_df.at[row, 'Steelworkkg_m2'] = summary_df.at[row, 'Steelworkkg_m2']
    else:
        # If "RC" is not present in the row name, multiply Steelworkkg_m2 by 1.1
        summary_df.at[row, 'Steelworkkg_m2'] = summary_df.at[row, 'Steelworkkg_m2'] * 1.1


#Reorder the dataframe to match the excel summary
# Define the desired row order
desired_row_order = [
    'RCFlatSlab',
    'PTRCFlatSlab',
    'RCRibSlab',
    'Two_wayRCSlab',
    'One_WaySpanningRC',
    'PrecastHollowcorewithIn_situRCBeams',
    'Non_CompositeRolledSteelwithPCCPlanks',
    'CompositeRolledSteelwithMetalDecking',
    'CompositeCellBeamswithMetalDecking',
    'SteelFramewithCLTSlabs',
    'CLTGlulamandSteelColumnHybrid',
]

# Reorder the rows in the summary DataFrame
summary_df = summary_df.loc[desired_row_order]






