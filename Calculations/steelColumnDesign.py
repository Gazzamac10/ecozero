#import pandas as pd
#from input import storeys, floorArea, building_use, building_useArr, floorToCeiling, columnsInternal, columnCorners, columnEdges, gk, qk
#from database import summary_df
##from calcDefs import factoredLoads
#import math
#
##Calculated RC Column Loads - output as dataframe
#steelColumnLoads = summary_df.copy()
## Filter out rows that do not contain 'RC' in the row index
#steelColumnLoads = steelColumnLoads[~steelColumnLoads.index.str.contains('RC')]
#
#
#steelColumnLoads = factoredLoads(steelColumnLoads,gk,qk,storeys)
#print(steelColumnLoads)
#
##Note calculated values between CA and CF need redoing
##Typologies need redoing too