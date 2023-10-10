import pandas as pd
import streamlit as st
from tools import graph_maker
from PIL import Image
import xlwings as xw
import pythoncom
file = 'Database/EcoZero Tool_v2_unlocked_GUI.xlsm'

def changeexcel(fp,xg,yg,xb,yb,sto):
    pythoncom.CoInitialize()
    # Open the workbook
    xw.App(visible=False)
    wb = xw.Book(fp)

    sht = wb.sheets["Summary"].activate()
    # Select the active sheet
    sht = wb.sheets.active
    # Update the value of a cell
    sht.range('C13').value = xg
    sht.range('C14').value = yg
    sht.range('C15').value = xb
    sht.range('C16').value = yb
    sht.range('C17').value = sto
    # Save the changes
    #return wb.app.status_bar
    #pythoncom.CoInitialize()
    wb.save()

    wb.close()

st.set_page_config (layout="wide")

file = 'Database/EcoZero Tool_v2_unlocked_GUI.xlsm'

image5  = Image.open('Images/EcoZero.JPG')
resized_image = image5.resize((300, 300))

dict = {'lat' : [51.509865], 'lon' : [ -0.118092]}

map = pd.DataFrame.from_dict(dict,orient='columns')


col1, col2 = st.columns([0.25,0.75])
with col1:
    st.image(resized_image)
with col2:
    st.map(map,zoom=14, use_container_width=True)


XG = st.slider('Grid_X', 5, 8, 12)
YG = st.slider('Grid_Y', 5, 8, 12)
#BaysX = st.slider('Bays_X', 5, 8, 12)
#BaysY = st.slider('Bays_Y', 5, 8, 12)
storeys = st.slider('No of Storeys', 1, 10, 20)

def updatetabel():
    df = pd.read_excel(file, sheet_name='Summary')
    table = df.iloc[73:85,2:4].reset_index(drop=True)
    headers = table.iloc[0].values
    table.columns = headers
    table.drop(index=0, axis=0, inplace=True)
    graph1 = graph_maker.plotlyBar(table, 'Typology', 'Est. Cost')
    graph1.update_layout(height=500)
    return table,graph1

changeexcel(file,XG,YG,None,None,storeys)

col1, col2 = st.columns([0.4,0.6])
with col1:
    st.dataframe(updatetabel()[0],width =None, height= None,use_container_width=True)
with col2:
    st.plotly_chart(updatetabel()[1], use_container_width=True)

