def numArray(start,end):
    arr = []
    for i in range(start,end+1):
        arr.append(i)
    return arr

# User Inputs to Summary Sheet. Switch out with web input
#Project Data
building_useArr = ['Office','Residential','Education','Healthcare']
building_use = building_useArr[0] #Default Value
country = 'UK'

#Geometry
gridXArr = numArray(5,12)
gridX = gridXArr[int((len(gridXArr))/2)] # Default value as mid of array

gridYArr = numArray(5,13)
gridY = gridYArr[int((len(gridYArr))/2)] # Default value as mid of array

bayXArr= numArray(1,20)
bayX = bayXArr[int((len(bayXArr))/2)] # Default value as mid of array

bayYArr = numArray(1,20)
bayY = bayYArr[int((len(bayYArr))/2)] # Default value as mid of array

storeys = '4' #  default value
floorToCeiling = 3 # default value

#Engineering Parameters
pileMethod = ['Continuous Flight Auger','Bored Cast in Place Concrete','Driven Precast Concrete','All Types']
concMixArr = ['C32/40 - CEM I (OPC)','C32/40 - 25% GGBS', 'C32/40 - 50% GGBS','C32/40 - 75% GGBS']
concMix = concMixArr[0] #  Default value
steelManufacture = ['Basic Oxygen Furnace','Electric Arc Furnace']

#GroundModelInputs
stratumType = ['Made Ground','Soft Clay','Firm Clay','Stiff Clay','Very Stiff Clay','Hard Clay','Silt','Loose Sand/Gravel','Medium Sand/Gravel','Dense Sand/Gravel','Low Density Chalk','Medium Density Chalk','High Density Chalk','None']
stratumThickness = 1 # default value m

averageSurfaceLevel = 0 # default value m
groundwaterLevel = 0 # default value m

#Transfer Deck Requicments

transferDeck = ['Yes','No']
tSlabDepth = [1] #default m
tRebarRate = 0 #default kg/m3

# Basement Requirements
basement = ['Yes','No']
depth = 5 #default value formation level in m BGL
props = ['Yes','No']

def wallPileDiameter(depth):
    if depth <= 6:
        return 600
    elif depth <= 7.5:
        return 750
    elif depth <= 9:
        return 900
    elif depth <= 10.05:
        return 1050
    elif depth <= 12:
        return 1200
    else:
        return 0
wallPileDia = wallPileDiameter(depth)

#Facade Data
facadeTypeArr =['Cavity Wall','Lightweight Cladding','Curtain Walling','Timber Cladding','Timber Cladding']
facadeType = facadeTypeArr[2] # default value
glazingPercentage = 25 #default value %

#Design Types
typologyArr = ['Two-way RC Slab', 'One-Way Spanning RC', 'Precast Hollowcore with In-situ RC Beams','Non-Composite Rolled Steel with PCC Planks', 'Composite Rolled Steel with Metal Decking','Composite Cell Beams with Metal Decking','Steel Frame with CLT Slabs','CLT, Glulam and Steel Column Hybrid']
typology = typologyArr[3] # default value

#GUI Inputs
xGrid = gridX
yGrid = gridY
floorArea = 4 * xGrid * yGrid
floorCeilingHeight = floorToCeiling
noOfStoreys = storeys
columnsInternal = 1 #default
columnCorners = 4 #default
columnEdges = 4 #default
structuralSystem = typology
perimiter = 56 # default value
GIA = 540 #default value
buildingUse = building_use
boxX = 2*xGrid
boxY = 2*yGrid
lengthOfPrimaryBeams = 30 # default to be overwritten with calc
lengthofSecondaryBeams = 54 #default to be overwritten with calc


#Non changing input variables
perReinforcement = 4 # default value
gk = 1.35
qk = 1.5