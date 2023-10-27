#This is to be the checking sheet going forward in the repathing exercise. 

from DatabaseImport import databaseR, databaseSL
from Calculations import rcColumnDesign, steelColumnDesign
from Shear import Walls
from InputR import designTypology, gridX,gridY,building_use,facadeType, floorToCeiling, designTypology


#Summary Calc Table
#print(databaseR.summary_df)


#RC Column Design Dataframes
#print(rcColumnDesign.rcColumnLoads) #RC Column Load 

print(rcColumnDesign.InternalRcColumn) # Internal Column Design
#print(rcColumnDesign.EdgeRcColumn) # Edge Column Design
#print(rcColumnDesign.CornerRcColumn) # Corner Column Design

#print(rcColumnDesign.ColumnSummary) # Summary of RC Column Design

#print(steelColumnDesign.steelColumnLoads)


#Working Checks

#print(Walls.typologyAlt)
#print(databaseR.summary_df)
#print(Walls.corresponding_type)
#print(Walls.structural_zone)
#print(Walls.storeyHeight)

print(databaseSL.SummaryTable(gridX,gridY,building_use,facadeType,floorToCeiling,designTypology))



