#This is to be the checking sheet going forward in the repathing exercise. 

from DatabaseImport import databaseSL
from Calculations import  rcColumnDesignSL
from Shear import Walls
from InputR import stratumThicknessL1,depth,averageSurfaceLevel,groundWaterLevel, stratumType, stratumThicknessL2,stratumThicknessL3,stratumThicknessL4,groundWaterLevel,designTypology, gridX,gridY,building_use,facadeType, floorToCeiling, designTypology, gk,qk,concMix,storeys,floorArea,perReinforcement,building_use,bayX,bayY, averageSurfaceLevel
from Ground import Pile

print(Pile.pileGroundModel)
print(Pile.groundwaterLevel)








