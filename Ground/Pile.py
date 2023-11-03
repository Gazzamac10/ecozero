import pandas as pd
from DatabaseImport import databaseSL
import InputR
from Ground import GroundModel
import math
#Create Ground Model for three types of pile

# can be one def but needs to take type of pile as an input and run different if's on the calculated values.

#Eurocode Partial Factors for Pile Shafts and Bases (DA1-2)
#1 CFA/Bored Piles Partial Factors: R4 (without explicit verification of SLS)
EC_PF_CFABored = {
    "FactorType": ['Model Factor','Partial Resistance Factor'],
    "ForPileShaft": [1.4,1.6],
    "ForPileBase": [1.6,2.0]
}

ECPartialFact_CFABored = pd.DataFrame(EC_PF_CFABored)

#2 Driven Piles Partial Factors: R4 (without explicit verification of SLS)
EC_PF_Driven = {
    "FactorType": ['Model Factor','Partial Resistance Factor'],
    "ForPileShaft": [1.4,1.5],
    "ForPileBase": [1.5,1.7]
}

ECPartialFact_Driven = pd.DataFrame(EC_PF_Driven)

#Suggested Values of K0 and Ks for piles installed in coarse soils

coarseSoilPileVals = {
    "PileType":["Bored Cast in Place Concrete",'Conitinuous Flight Auger (CFA)','Conitinuous Flight Auger (CFA)','Driven Precast Concrete'] ,
    "SoilType": ['All Types','Silt','Sand','All Types'],
    "Ko":[1.0,1.0,1.0,0.67],
    "Ks":[0.7,0.6,0.9,1.1]
}


#Structural Capcity of each Diameter Piles - presumed  Eurocode Standards by Structures Team

pStructCap ={
    "PileDia":[450,600,750,900,1050,1200],
    "dnom":[427.5,570,712.5,855,997.5,1140],
    "Nrd":[2366.176187,4206.535443,6572.71163,9464.704747,12882.5148,16826.14177]    
}


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
layer2 = InputR.stratumType[-2]
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
pileGroundModel['Adhesion_Factor'] = pileGroundModel['material_value'].apply(lambda x: 0.5 if x == 'Cohesive' else 0)
pileGroundModel['Nc'] = pileGroundModel['material_value'].apply(lambda x: 9 if x == 'Cohesive' else 0)
#Design Paramaeters
updatedColumnNames = {
    'topUndrainedShearStrength':'Cu_at_top',
    'btmUndrainedShearStrength':'Cu_at_bottom'
}

#Granular Nq
#if material type is granular and stratum is not Made ground, exponential(pi * tan of angle of friction)* pi/180) *tan(45+angle of friction/2*pi/180) ^2

pileGroundModel.rename(columns=updatedColumnNames,inplace=True)

# Define a function to calculate Nq based on the equation and conditions
  
def calculate_Nq(row):
    if row['material_value'] == 'Granular' and row.name != 'Made Ground':
        AngleofFriction = float(row['angleOfFriction'])
        Calc = (math.exp(math.pi * (math.tan((AngleofFriction) * math.pi / 180)))) * (math.tan((45 + AngleofFriction/2)*math.pi/180)**2)
        return Calc
    else:
        return 0


# Create the new "Nq" column using the function
pileGroundModel['Nq'] = pileGroundModel.apply(calculate_Nq, axis=1)


#KtanDelta 

#Def for if Silt, Loose Sand/Gravel, Medium Sand/Gravel, Dense Sand/Gravel
def KtanDelta(pileType,coarseSoilPileVals, angleoffriction):

    for i, pile_type in enumerate(coarseSoilPileVals['PileType']):
        if pile_type == pileType:
            ko = (coarseSoilPileVals['Ko'][i])
            ks = (coarseSoilPileVals['Ks'][i])
    ktandelta = ks * (math.tan(ko*int(angleoffriction)*(math.pi/180)))
    return ktandelta

allowed_soil_types = ['Silt', 'Loose Sand/Gravel', 'Medium Sand/Gravel', 'Dense Sand/Gravel']

def compute_kTanDelta(row, coarseSoilPileVals, allowed_soil_types, pile_type):  
    if row.name in allowed_soil_types:
        return KtanDelta(pile_type, coarseSoilPileVals, row['angleOfFriction'])
    else:
        return 0


pile_type = 'Bored Cast in Place Concrete'
pileGroundModel['kTanDelta'] = pileGroundModel.apply(compute_kTanDelta, args=(coarseSoilPileVals, allowed_soil_types,pile_type), axis=1)

def calculate_TsfBeta(row):
    if row.name == 'Low Density Chalk' or row.name == 'Medium Density Chalk':
        
        return 0.8
    else:
        return 0

pileGroundModel['TsfBeta'] = pileGroundModel.apply(calculate_TsfBeta, axis=1)

def compute_0_1_qc(row):
    if row.name == 'High Density Chalk':
        return 0.1 * float(row['UCS_ChalkSaturated']) if groundwaterLevel > row['btmStratumLevel'] else 0.1 * float(row['UCS_Chalk'])
    else:
        return 0

pileGroundModel['0.1qc'] = pileGroundModel.apply(compute_0_1_qc, axis=1)

def N_200(row):
    if row['material_value'] == 'Chalk':
        return float(row['SPTChalk'])*200
    else:
        return 0
pileGroundModel['200N']=pileGroundModel.apply(N_200,axis=1)


#Limits need to check on the type of pile
#Limit on design shaft stress


#Limit on charactersitic shaft stress


#Limit on design base stress


#Limit on characteristic base stress