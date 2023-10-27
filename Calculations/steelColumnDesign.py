import pandas as pd
from InputR import storeys, gk, qk
from DatabaseImport import databaseR
from Defs import definitions
import pandas as pd
import math

#Calculated RC Column Loads - output as dataframe
steelColumnLoads =  databaseR.summary_df.copy()
# Filter out rows that do not contain 'RC' in the row index
steelColumnLoads = steelColumnLoads[~steelColumnLoads.index.str.contains('RC')]

#Steel Column Load Output
steelColumnLoads = definitions.factoredLoads(steelColumnLoads,gk,qk,storeys)

#Calculate Ref Row from UC-Axial Table
#Ref Row is a calculation from the different Typologies

##Note calculated values between CA and CF need redoing
##Typologies need redoing too