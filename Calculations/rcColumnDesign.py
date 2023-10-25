import pandas as pd
from InputR import storeys, concMix, perReinforcement, floorArea, building_use, building_useArr, floorToCeiling, columnsInternal, columnCorners, columnEdges, gk, qk
from DatabaseImport import databaseR
from Defs import definitions
import pandas as pd
import math

#GeneralLoading



#RCColumns
def columnRCDesign(loadDf,InternalEdgeCorner,columnNumber,storeys,storeyHeight,percentageReinforcement,planArea,rcGrade,minD):
    if(InternalEdgeCorner=='Corner'):
        col = 'CornerNed'
    elif(InternalEdgeCorner=='Edge'):
        col = 'EdgeNed'
    else:
        col = 'InternalNed'
    Name = loadDf[[col]].copy()
    Name['calculatedValue'] = Name[col] / ((0.4 * rcGrade + 0.75 * 500 * (percentageReinforcement)) / 1000)
    Name['D'] = Name['calculatedValue'].apply(lambda x: max(minD, math.ceil(math.sqrt(x) / 25) * 25))
    Name['CSArea'] =  Name['D']*Name['D']
    Name['Concrete'] = (columnNumber * ((Name['CSArea']/1000000)*23*storeyHeight*1000/9.81))/planArea
    Name['RebarKG_m2'] = (columnNumber*7850*(Name['CSArea']/1000000)*percentageReinforcement*storeyHeight)/planArea
    Name['ColumnSW'] = (Name['CSArea']/1000000)*25*storeyHeight*storeys
    Name['ConcreteVolume'] =  (Name['CSArea']/1000000)*storeyHeight*storeys*columnNumber
    Name['Rebar'] = Name['ConcreteVolume']*percentageReinforcement*7850*0.001
    Name['Formwork']= columnNumber*storeys*storeyHeight*4*Name['D']/1000 
    return Name


#Calculated RC Column Loads - output as dataframe
rcColumnLoads = databaseR.summary_df.copy()
# Filter out rows that do not contain 'RC' in the row index
rcColumnLoads = rcColumnLoads[rcColumnLoads.index.str.contains('RC')]
# Calculate factored reactions

rcColumnLoads = definitions.factoredLoads(rcColumnLoads,gk,qk,storeys) 
#output rcColumnLoads is dataframe for processing

#Column Design
rcGrade = int(concMix.split('/')[1][:2])
print(rcGrade)

planArea = floorArea
storeyHeight = floorToCeiling

#Fire Rating - could be useful to show as output.
#minD is column design
#Note this only allows two inputs based on building type, it will need recording to allow for more fire situations
if building_use == building_useArr[1]:
    fireRating = 120
    minD = 350
else:
    fireRating = 60
    minD = 250
    
percentageReinforcement = perReinforcement/100
   
#Internal Colulumn Design
InternalRcColumn = columnRCDesign(rcColumnLoads,'Internal',columnsInternal,storeys,storeyHeight,percentageReinforcement,planArea,rcGrade,minD)

#EdgeColumnDesign
EdgeRcColumn = columnRCDesign(rcColumnLoads,'Edge',columnEdges,storeys,storeyHeight,percentageReinforcement,planArea,rcGrade,minD)

#CornerColumnDesign
CornerRcColumn = columnRCDesign(rcColumnLoads,'Corner',columnCorners,storeys,storeyHeight,percentageReinforcement,planArea,rcGrade,minD)

#Totals
ColumnSummary = CornerRcColumn.copy()
columns_to_sum = ['Concrete', 'RebarKG_m2', 'ConcreteVolume', 'Rebar', 'Formwork']
for col in columns_to_sum:
    ColumnSummary[col] = InternalRcColumn[col] + EdgeRcColumn[col] + CornerRcColumn[col]

for col in ColumnSummary.columns:
    if col not in columns_to_sum:
        ColumnSummary.drop(col, axis=1, inplace=True)

#Pile Loads (Excludes Pile Loads)

#Adjust Summary
rcSummary = databaseR.summary_df.copy()
# Filter out rows that do not contain 'RC' in the row index
rcSummary = rcSummary[rcSummary.index.str.contains('RC')]


columnIntSw = InternalRcColumn['ColumnSW']
columnIntSw = columnIntSw.rename('InternalColumnSw')
columnEdSw = EdgeRcColumn['ColumnSW']
columnEdSw = columnEdSw.rename('EdgeColumnSw')
columnCorSw = CornerRcColumn['ColumnSW']
columnCorSw = columnCorSw.rename('CornerColumnSw')

pileLoads = pd.concat([columnIntSw,columnEdSw,columnCorSw, rcSummary], axis=1, join='outer')

# Create the new 'pLGk' column based on your condition
pileLoads['pLGkInt'] = pileLoads.apply(
    lambda row: 0 if row['StructuralZonem'] == 0 else (row['InternalColumn_Gk_kN'] * storeys + row['InternalColumnSw']),
    axis=1
)
pileLoads['pLQkInt'] = pileLoads['InternalColumn_Qk_kN']*storeys
pileLoads['pLGkEd'] = pileLoads.apply(
    lambda row: 0 if row['StructuralZonem'] == 0 else (row['EdgeColumn_Gk_kN'] * storeys + row['EdgeColumnSw']),
    axis=1
)
pileLoads['pLQkEd'] = pileLoads['EdgeColumn_Qk_kN']*storeys
pileLoads['pLGkCor'] = pileLoads.apply(
    lambda row: 0 if row['StructuralZonem'] == 0 else (row['CornerColumn_Gk_kN'] * storeys + row['CornerColumnSw']),
    axis=1
)
pileLoads['pLQkCor'] = pileLoads['CornerColumn_Qk_kN']*storeys
internal_columns_to_keep = ['pLGkInt','pLQkInt','pLGkEd','pLQkEd','pLGkCor','pLQkCor']
pileLoads = pileLoads[internal_columns_to_keep]

print(ColumnSummary)

