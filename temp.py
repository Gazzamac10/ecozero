import pandas as pd

# Create a sample Pandas DataFrame
data = {
    'A': [1, 2, 3, 4, 5],
    'B': ['Apple', 'Banana', 'Cherry', 'Date', 'Fig'],
    'C': [0.1, 0.2, 0.3, 0.4, 0.5],
    'D': [True, False, True, False, True],
    'E': [10, 20, 30, 40, 50],
}

df = pd.DataFrame(data)


print (df)

# Specify the output JSON file path
json_file_path = 'output.json'

# Save the DataFrame as a JSON file
#df.to_json(json_file_path, orient='records', lines=True)

print(f"Data has been saved to {json_file_path}")




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
    storeys = st.text_input('Storeys', '3')
with col2:
    gridYarray = st.selectbox('Grid_Y', InputR.gridYArr)
    baysYarray = st.selectbox('Bays_Y', InputR.bayYArr)
floorToCeiling = st.sidebar.text_input('Floor To Ceiling Height', '2')

 #st.sidebar.divider()
with st.sidebar.expander('Engineering Data'):
    Piling_Meth = st.selectbox('Piling_Methodology', InputR.pileMethod)
    concMixArr = st.selectbox('Concrete Mix', InputR.concMixArr)
    steelManufacture = st.selectbox('Steel Manufacture', InputR.steelManufacture)
    
    
    
    
    
import streamlit as st
from tools import input

class SidebarInputs:
    def __init__(self):
        self.Project_Reference = None
        self.Building_Use = None
        self.Country = 'UK'
        self.Grid_X = None
        self.Bays_X = None
        self.Storeys = '3'
        self.Grid_Y = None
        self.Bays_Y = None
        self.Floor_To_Ceiling_Height = '2'
        self.Piling_Methodology = None
        self.Concrete_Mix = None
        self.Steel_Manufacture = None

    def render(self):
        st.sidebar.markdown('<h3>USER INPUT</h3>', unsafe_allow_html=True)
        st.sidebar.markdown('<h3>Project Data</h3>', unsafe_allow_html=True)
        self.Project_Reference = st.sidebar.text_input('Project Reference', self.Project_Reference)
        col1, col2 = st.sidebar.columns(2)
        with col1:
            self.Building_Use = st.selectbox('Building Use', input.building_useArr)
        with col2:
            self.Country = st.text_input('Country', self.Country)
        st.sidebar.markdown('<h3>Geometry</h3>', unsafe_allow_html=True)
        col1, col2 = st.sidebar.columns(2)
        with col1:
            self.Grid_X = st.selectbox('Grid_X', input.gridXArr)
            self.Bays_X = st.selectbox('Bays_X', input.bayXArr)
            self.Storeys = st.text_input('Storeys', self.Storeys)
        with col2:
            self.Grid_Y = st.selectbox('Grid_Y', input.gridYArr)
            self.Bays_Y = st.selectbox('Bays_Y', input.bayYArr)
            self.Floor_To_Ceiling_Height = st.text_input('Floor To Ceiling Height', self.Floor_To_Ceiling_Height)

        with st.sidebar.expander('Engineering Data'):
            self.Piling_Methodology = st.selectbox('Piling Methodology', input.pileMethod)
            self.Concrete_Mix = st.selectbox('Concrete Mix', input.concMixArr)
            self.Steel_Manufacture = st.selectbox('Steel Manufacture', input.steelManufacture)

# Create an instance of the SidebarInputs class
sidebar = SidebarInputs()

# Render the sidebar to capture the input values
sidebar.render()

# Access the input values
#d = sidebar
#t = sidebar.Grid_X
