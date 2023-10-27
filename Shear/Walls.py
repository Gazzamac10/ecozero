import pandas as pd
from InputR import building_use, designTypology, floorToCeiling
from DatabaseImport import databaseR

#Static Data
terCat = {
    "Category": [0, 1, 2, 3, 4],
    "Z0": [0.003, 0.01, 0.05, 0.3, 1],
    "Zmin": [1, 1, 2, 5, 10]
}

terrainCatagory = pd.DataFrame(terCat)

singBarArea = {
    "BarSize":['H10','H12','H16','H20','H25'],
    "As":[78.5, 113.1, 201.1, 314.2, 490.9]
}
singleBarArea = pd.DataFrame(singBarArea)

wallThk = {
    "Building":[0,24,42,60,80,100,120,140,160,180],
    "Thickness":['0mm','200mm','250mm','300mm','350mm','400mm','450mm','500mm','550mm','600mm']
}

wallThickness = pd.DataFrame(wallThk)

#RC Flat Slab, but this needs to be converted to a def

typology = 1
typologyAlt = "RCFlatSlab" # this can be changed to be the value from the summary_df table

#the def needs to start here and include typologyalt

floorFinishServiceZone = databaseR.ffSZ

if building_use in floorFinishServiceZone.columns:
    selected_column = floorFinishServiceZone[building_use].astype(float) * 0.001
    selected_column_name = building_use  # Store the selected column name
    description_column = floorFinishServiceZone['Description']  # Get the 'Description' column
    floorZones = pd.DataFrame({'Description': description_column, selected_column_name: selected_column})
    
else:
    print(f"'{building_use}' is not a valid column name.")
    
#find the type name to match, because they don't line up
index = designTypology['altTypes'].index(typologyAlt)
corresponding_type = designTypology['Type'][index]

# Filter the DataFrame by matching the "Description" column
filtered_rows = floorZones[floorZones['Description'] == corresponding_type]

#get the value of the services and finisheszone
if not filtered_rows.empty:
    sfZone = filtered_rows.iloc[0, -1]  
    
else:
    print(f"No matching rows found for '{corresponding_type}'.")
    

if typologyAlt in databaseR.summary_df.index:
    # Use the typologyAlt to find the corresponding "StructuralZone" value
    structural_zone = databaseR.summary_df.loc[typologyAlt, 'StructuralZonem']
else:
    print(f"No match found for '{typologyAlt}' in the summary_df index.")

storeyHeight = floorToCeiling+structural_zone+sfZone

#STOP REDO THE CARBON FACTORS