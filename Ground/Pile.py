import pandas as pd
from DatabaseImport import databaseSL
import InputR
from Ground import GroundModel
#Create Ground Model for three types of pile

# can be one def but needs to take type of pile as an input and run different if's on the calculated values.

#Pile Type
#pileMethod = InputR.pileMethod[0]

gmdb = databaseSL.tableDB('GroundModelDB')
#Gonna need this variable as a user input

basementDepth = InputR.depth

basementInput = False

#Inputs need to be replaced by user drop downs chosed from the stratumType and StratumThickness Arrays in InputR
#Layer 1 
layer1 = InputR.stratumType[0]
stratumThicknessL1 = InputR.stratumThicknessL1
#Layer 2
layer2 = InputR.stratumType[2]
stratumThicknessL2 = InputR.stratumThicknessL2
#Layer 3
layer3 = InputR.stratumType[6]
stratumThicknessL3 = InputR.stratumThicknessL3
#Layer 4
layer4 = InputR.stratumType[1]
stratumThicknessL4 = InputR.stratumThicknessL4

layers = [layer1,layer2,layer3,layer4]
layerThickness = [stratumThicknessL1,stratumThicknessL2,stratumThicknessL3,stratumThicknessL4]

#Average Surface Level and Ground Water Level should be user inputs, default surface level 0, default groundwater level 0
groundModelTable = GroundModel.gmSurfaceLevelDF(layers,layerThickness,gmdb,InputR.averageSurfaceLevel,InputR.groundWaterLevel)
basementGroundModelTable = GroundModel.gmBasementDF(basementDepth,layers,layerThickness,gmdb,InputR.averageSurfaceLevel,InputR.groundWaterLevel)
groundwaterLevel = GroundModel.groundwater(InputR.averageSurfaceLevel,InputR.groundWaterLevel)[1]
# start of the def - above needs to be from the inputs or referenced elsewhere

# Work out which ground model is needed
if basementInput:
    pileGroundModel = basementGroundModelTable
else:
    pileGroundModel = groundModelTable
    
pileGroundModel['UnitWeight'] = pileGroundModel.apply(lambda row: row['satUnitWeight'] if groundwaterLevel > row['btmStratumLevel'] else row['dryUnitWeight'], axis=1)



#First two columns are the same -  Unit weight of material
#load the ground water, check the level, then call the unit weight as either dry or saturted.
#Assumption if water level is in a part of the strata, aka above the btm level of the strata then take the saturated unit weight

