#This is to be the checking sheet going forward in the repathing exercise. 

from DatabaseImport import databaseSL
from Calculations import  rcColumnDesignSL
from Shear import Walls
from InputR import designTypology, gridX,gridY,building_use,facadeType, floorToCeiling, designTypology, gk,qk,concMix,storeys,floorArea,perReinforcement,building_use,bayX,bayY


#print(databaseSL.SummaryTable(gridX,gridY,building_use,facadeType,floorToCeiling,designTypology))
db = (databaseSL.SummaryTable(gridX,gridY,building_use,facadeType,floorToCeiling,designTypology))
columnDesign = rcColumnDesignSL.rcColumnDesign(db,gk,qk,concMix,storeys,floorToCeiling,perReinforcement,building_use,bayX,bayY,gridX,gridY)
print(columnDesign[1])

