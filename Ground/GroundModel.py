import pandas as pd

#Import the ground model database

def groundwater(averageSurfaceLevel,groundWaterLevel):
    gwAOD = averageSurfaceLevel - groundWaterLevel
    return groundWaterLevel, gwAOD

 
def gmCalc(gmDB,stratumType,avSurfaceLevel,stratumThickness,stratumThicknessAbove,groundWaterLevel):
    # Filter the DataFrame based on the condition
    def replace_slash_with_underscore(stratumType):
        return stratumType.replace('/', '_')
    stratumType = replace_slash_with_underscore(stratumType)
    filtered_row = gmDB[gmDB['RowKey'] == stratumType]
    # Retrieve the value from the 'Type_of_Material' column
    material_value = filtered_row['Type_of_Material'].values[0] if not filtered_row.empty else None
    satUnitWeight = filtered_row['Unit_Weight_Saturated'].values[0] if not filtered_row.empty else None
    dryUnitWeight = filtered_row['Unit_Weight_Dry'].values[0] if not filtered_row.empty else None
    topUndrainedShearStrength = filtered_row['Undrained_Shear_Strength'].values[0] if not filtered_row.empty else None
    btmUndrainedShearStrength = topUndrainedShearStrength
    angleOfFriction = filtered_row['Internal_Angle_of_Friction'].values[0] if not filtered_row.empty else None
    uniaxialCompressiveStrength = filtered_row['Uniaxial_Compressive_Strength'].values[0] if not filtered_row.empty else None
    SPTChalk = filtered_row['SPT_N_Value_for_Chalk'].values[0] if not filtered_row.empty else None
    if material_value is not None:
        material_value= material_value
        satUnitWeight = satUnitWeight 
        dryUnitWeight = dryUnitWeight      
    else:
        print(f'No matching RowKey found for {stratumType}')
    linearStrengthEq = 'No Equation' # Note this is regardless of input and is hardcoded  
    
    if material_value =='None':
        topStratumLevel = 0
        thkstrata = 0
        strength = 'Linear'
        
    else:
        topStratumLevel = avSurfaceLevel - stratumThicknessAbove
        strength = 'Constant' 
        thkstrata = stratumThickness 
    
    btmStratumLevel = topStratumLevel - thkstrata - stratumThicknessAbove
    
    if(groundWaterLevel<abs(btmStratumLevel)):
        #then the stratum is in water...so
        UCS_Chalk = 0
        UCS_ChalkSaturated  = filtered_row['Unconfined_Compressive_Strength_Saturated_Chalk'].values[0] if not filtered_row.empty else None
    else:
        UCS_Chalk =  filtered_row['Unconfined_Compressive_Strength_DryChalk'].values[0] if not filtered_row.empty else None
        UCS_ChalkSaturated = 0
        # equation isn't right in the excel
    # this needs to be that if the strata is in the water then dry is zero and saturdted has a value 
        
    # if the material value is not cohesive then 0, if it's cohesive then get from the database
    
    return material_value, topStratumLevel, thkstrata, btmStratumLevel,satUnitWeight,dryUnitWeight,topUndrainedShearStrength, btmUndrainedShearStrength, angleOfFriction, uniaxialCompressiveStrength, UCS_Chalk, UCS_ChalkSaturated, SPTChalk


def gmSurfaceLevelDF(layers,layerThickness,gmDB,avSurfaceLevel,groundWaterLevel):
    column_names = ["material_value", "topStratumLevel", "thkstrata", "btmStratumLevel",
                "satUnitWeight", "dryUnitWeight", "topUndrainedShearStrength",
                "btmUndrainedShearStrength", "angleOfFriction", "uniaxialCompressiveStrength",
                "UCS_Chalk", "UCS_ChalkSaturated", "SPTChalk"]
    groundModelTable = pd.DataFrame(columns=column_names)
    stratumThicknessAbove = 0 #Start theStratumThickness above at 0
    index_values = []  # Accumulate index values in a list

    for layer, thickness in zip(layers, layerThickness):
        # Calculate the layer properties using gmCalc
        result = gmCalc(gmDB, layer, avSurfaceLevel, thickness, stratumThicknessAbove, groundWaterLevel)

        # Append the result to the DataFrame
        groundModelTable = groundModelTable.append(pd.Series(result, index=column_names), ignore_index=True)
        index_values.append(str(layer))  # Append index values to the list

        # Update stratumThicknessAbove for the next layer
        stratumThicknessAbove += thickness

    groundModelTable.index = index_values  # Set the index once with the accumulated values

    return groundModelTable

def gmBasementDF(basementDepth,layers,layerThickness,gmDB,avSurfaceLevel,groundWaterLevel):
    #startingLevel
    #so this needs to start by checking what layer the basment is in. 
      basemodel = gmSurfaceLevelDF(layers,layerThickness,gmDB,avSurfaceLevel,groundWaterLevel)
      basementModel = basemodel[basemodel['btmStratumLevel'] <= basementDepth * -1]
      return basementModel