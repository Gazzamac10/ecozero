import streamlit as st
from tools import input

Project_Ref = ''
Building_Use = 'Office'
gridXarray = 5
gridYarray = 10
baysXarray = 5
baysXarray = 5
baysYarray = 5
Storeys = 2
floorToCeiling = 3
Piling_Meth = 'All Types'
concMix = 'C32/40 - CEM I (OPC)'
steelManufacture = 'Basic Oxygen Furnace'
Layer1 = 'Made Ground'
stratumThicknessL1 = '6'
Layer2 = 'Firm Clay'
stratumThicknessL2 = '6'
Layer3 = 'Medium Sand/Gravel'
stratumThicknessL3 = '30'
Layer4 = 'Very Stiff Clay'
stratumThicknessL4 = '6'
averageSurfaceLevel = '5'
groundWaterLevel = '20'



def sidebar_inputs():
    
    global Project_Ref
    global Building_Use
    global gridXarray
    global gridYarray
    global baysXarray
    global baysYarray
    global Storeys
    global floorToCeiling
    global Piling_Meth
    global concMix
    global steelManufacture
    global Layer1
    global stratumThicknessL1
    global Layer2
    global stratumThicknessL2
    global Layer3
    global stratumThicknessL3
    global Layer4
    global stratumThicknessL4
    global averageSurfaceLevel
    global groundWaterLevel
    
    st.sidebar.markdown('''<h3>USER INPUT</h3>''', unsafe_allow_html=True)
    st.sidebar.markdown('''<h3>Project Data</h3>''', unsafe_allow_html=True)
    Project_Ref = st.sidebar.text_input('Project Reference', '')
    col1, col2 = st.sidebar.columns(2)
    with col1:
        Building_Use = st.selectbox('Building Use', input.building_useArr, index=input.building_useArr.index(Building_Use))
    with col2:
        st.text_input('Country', 'UK')
    st.sidebar.markdown('''<h3>Geometry</h3>''', unsafe_allow_html=True)
    col1, col2 = st.sidebar.columns(2)
    with col1:
        gridXarray = st.selectbox('Grid_X', input.gridXArr, index=input.gridXArr.index(gridXarray))
        baysXarray = st.selectbox('Bays_X', input.bayXArr, index=input.bayXArr.index(baysXarray))
        Storeys = st.text_input('Storeys', str(Storeys))
    with col2:
        gridYarray = st.selectbox('Grid_Y', input.gridYArr, index=input.gridYArr.index(gridYarray))
        baysYarray = st.selectbox('Bays_Y', input.bayYArr, index=input.bayYArr.index(baysYarray))
        floorToCeiling = st.sidebar.text_input('Floor To Ceiling Height', str(floorToCeiling))

    #st.sidebar.divider()
    with st.sidebar.expander('Engineering Data'):
        Piling_Meth = st.selectbox('Piling_Methodology', input.pileMethod, index=input.pileMethod.index(Piling_Meth))
        concMix = st.selectbox('Concrete Mix', input.concMixArr, index=input.concMixArr.index(concMix))
        steelManufacture = st.selectbox('Steel Manufacture', input.steelManufacture, index=input.steelManufacture.index(steelManufacture))
    
    with st.sidebar.expander('Ground Model Inputs'):
        col1, col2 = st.columns(2)
        with col1:
            Layer1 = st.selectbox('Layer 1', input.stratumType, index=input.stratumType.index(Layer1))
            Layer2 = st.selectbox('Layer 2', input.stratumType, index=input.stratumType.index(Layer2))
            Layer3 = st.selectbox('Layer 3', input.stratumType, index=input.stratumType.index(Layer3))
            Layer4 = st.selectbox('Layer 4', input.stratumType, index=input.stratumType.index(Layer4))
        with col2:
            stratumThicknessL1 = st.text_input('Thickness L1', str(stratumThicknessL1))
            stratumThicknessL2 = st.text_input('Thickness L2', str(stratumThicknessL2))
            stratumThicknessL3 = st.text_input('Thickness L3', str(stratumThicknessL3))
            stratumThicknessL4 = st.text_input('Thickness L4', str(stratumThicknessL4))
            
        averageSurfaceLevel = st.text_input('Average Surface level', str(averageSurfaceLevel))