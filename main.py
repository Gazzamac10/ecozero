#This is to be the checking sheet going forward in the repathing exercise. 

from DatabaseImport import databaseR
from Calculations import rcColumnDesign, steelColumnDesign


#Summary Calc Table
print(databaseR.summary_df)


#RC Column Design Dataframes
#print(rcColumnDesign.rcColumnLoads) #RC Column Load 

#print(rcColumnDesign.InternalRcColumn) # Internal Column Design
#print(rcColumnDesign.EdgeRcColumn) # Edge Column Design
#print(rcColumnDesign.CornerRcColumn) # Corner Column Design

#print(rcColumnDesign.ColumnSummary) # Summary of RC Column Design


#Steel Column Design Dataframes
#print(steelColumnDesign.steelColumnLoads)



#Working Checks


#print(steelColumnDesign.steelColumnLoads)

#Moving on to Shear Walls because of the fuckery
#Calculate shear walls, refernce into UC Axial, call into Steel Column Design. Absolute fuckery
