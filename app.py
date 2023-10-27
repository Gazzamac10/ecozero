import streamlit as st
import InputR
import numpy as np
from PIL import Image
import pandas as pd
from DatabaseImport import databaseSL
from Calculations import rcColumnDesignSL
from tools import graph_maker

st.set_page_config(page_title="My Streamlit App", page_icon=":rocket:", layout="wide", initial_sidebar_state="expanded")

# Add custom CSS styles
st.markdown(
    """
    <style>
        a {
        color: black;
        font-family: Adobe Thai;
        font-size: 18px;
        text-align: left;
        }   
        h1 {
            color: white;
            font-family: Adobe Thai;
            font-size: 78px;
            text-align: left;
        }
        h2 {
            font-weight: bold;
            color: #849855;
            font-family: Arial, sans-serif;
            font-size: 30px;
            text-align: left;

        p {
            color: Black;
            font-family: Arial, sans-serif;
            font-size: 24px;
            text-align: left;
        }
        p1 {
            color: Black;
            font-weight: bold;
            font-family: Arial, sans-serif;
            font-size: 18px;
            text-align: left;
        }
        p2 {
            color: Black;
            font-family: Arial, sans-serif;
            font-size: 18px;
            text-align: left;
            padding-left: 25px 
        }
        p3 {
            color: Red;
            font-family: Arial, sans-serif;
            font-size: 18px;
            text-align: left;
            #margin-bottom: 24px;
        }
        p4 {
            color: #d43a2e;
            font-family: Arial, sans-serif;
            font-size: 18px;
            text-align: left;
            #margin-bottom: 24px;
        }
        p5 {
            color: #86325b;
            font-family: Arial, sans-serif;
            font-size: 24px;
            text-align: left;
            #margin-bottom: 24px;
        }
        dummy {
            color: White;
            font-family: Arial, sans-serif;
            font-size: 18px;
            text-align: left;
            #line-height: 0.15;
            #margin-bottom: 0px;
        }
        .katex-html {
            text-align: left;
            font-size: 22px;
            font-family: 'Times New Roman', Times, serif;
        }
    </style>
    """,
    unsafe_allow_html=True,
)

st.markdown('<dummy id="Home-1"></dummy>', unsafe_allow_html=True)
col1, col2 = st.columns([0.1,0.9])
#with col1:
    #imageecozero  = Image.open('images/EcoZero.JPG')
    #resized_image = imageecozero.resize((150, 150))
    #st.image(resized_image)
with col2:
    st.markdown("<h1>ECO.ZERO - Structure</h1>", unsafe_allow_html=True)
    st.markdown('<dummy id="UserInput-1"></dummy>', unsafe_allow_html=True)
#st.image('MV5BNzlhYjEzOGItN2MwNS00ODRiLWE5OTItYThiNmJlMTdmMzgxXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_.jpg')
st.divider()


st.sidebar.markdown('''<h3>USER INPUT</h3>''', unsafe_allow_html=True)
st.sidebar.markdown('''<h3>Project Data</h3>''', unsafe_allow_html=True)
st.sidebar.text_input('Project Reference', '')
col1, col2 = st.sidebar.columns(2)
with col1:
    Building_Use = st.selectbox('Building Use', InputR.building_useArr)
with col2:
    st.text_input('Country', 'UK')
st.sidebar.markdown('''<h3>Geometry</h3>''', unsafe_allow_html=True)
col1, col2 = st.sidebar.columns(2)
with col1:
    gridXarray = st.selectbox('Grid_X', InputR.gridXArr)
    baysXarray = st.selectbox('Bays_X', InputR.bayXArr)
    storeys = st.text_input('Storeys', '')
with col2:
    gridYarray = st.selectbox('Grid_Y', InputR.gridYArr)
    baysYarray = st.selectbox('Bays_Y', InputR.bayYArr)
    floorToCeiling = st.text_input('Floor To Ceiling Height', '2')

#st.sidebar.divider()
st.sidebar.markdown('''<h3>Engineering Data</h3>''', unsafe_allow_html=True)
Piling_Meth = st.sidebar.selectbox('Piling_Methodology', InputR.pileMethod)

# NOTE- facadeType and flootToCeiling need to be user inputs
db1 = databaseSL.SummaryTable(gridXarray,gridYarray,Building_Use,InputR.facadeType,InputR.floorToCeiling,InputR.designTypology)

st.write(db1)
db1 = db1.reset_index()
db1 = db1.rename(columns={'index': 'Typology'})


graph1 = graph_maker.plotlyBar(db1, 'Typology', 'CornerColumn_Gk_kN')
graph1.update_layout(height=500)

col1, col2 = st.columns([0.7,0.3])
with col1:
    st.plotly_chart(graph1, use_container_width=True)
