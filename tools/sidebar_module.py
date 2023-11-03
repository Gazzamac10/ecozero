import streamlit as st
from tools import input


def sidebar_inputs():
    
    session = st.session_state
    
    st.sidebar.markdown('''<h3>USER INPUT</h3>''', unsafe_allow_html=True)
    st.sidebar.markdown('''<h3>Project Data</h3>''', unsafe_allow_html=True)
    
    session.Project_Ref = st.sidebar.text_input('Project Reference', session.get('Project_Ref', ''))
    
    col1, col2 = st.sidebar.columns(2)
    with col1:
        session.Building_Use = st.selectbox('Building Use', input.building_useArr, index=input.building_useArr.index(session.get('Building_Use', 'Office')))
    with col2:
        st.text_input('Country', 'UK')
    
    st.sidebar.markdown('''<h3>Geometry</h3>''', unsafe_allow_html=True)
    
    col1, col2 = st.sidebar.columns(2)
    with col1:
        session.gridXarray = st.selectbox('Grid_X', input.gridXArr, index=input.gridXArr.index(session.get('gridXarray', 5)))
        session.baysXarray = st.selectbox('Bays_X', input.bayXArr, index=input.bayXArr.index(session.get('baysXarray', 5)))
        session.Storeys = st.text_input('Storeys', session.get('Storeys', '2'))
    
    with col2:
        session.gridYarray = st.selectbox('Grid_Y', input.gridYArr, index=input.gridYArr.index(session.get('gridYarray', 5)))
        session.baysYarray = st.selectbox('Bays_Y', input.bayYArr, index=input.bayYArr.index(session.get('baysYarray', 5)))
        session.floorToCeiling = st.sidebar.text_input('Floor To Ceiling Height', session.get('floorToCeiling', '3'))

    #st.sidebar.divider()
    with st.sidebar.expander('Engineering Data'):
        session.Piling_Meth = st.selectbox('Piling_Methodology', input.pileMethod, index=input.pileMethod.index(session.get('Piling_Meth', 'All Types')))
        session.concMix = st.selectbox('Concrete Mix', input.concMixArr, index=input.concMixArr.index(session.get('concMix', 'C32/40 - CEM I (OPC)')))
        session.steelManufacture = st.selectbox('Steel Manufacture', input.steelManufacture, index=input.steelManufacture.index(session.get('steelManufacture', 'Basic Oxygen Furnace')))
    
    with st.sidebar.expander('Ground Model Inputs'):
        col1, col2 = st.columns(2)
        with col1:
            session.Layer1 = st.selectbox('Layer 1', input.stratumType, index=input.stratumType.index(session.get('Layer1', 'Made Ground')))
            session.Layer2 = st.selectbox('Layer 2', input.stratumType, index=input.stratumType.index(session.get('Layer2', 'Firm Clay')))
            session.Layer3 = st.selectbox('Layer 3', input.stratumType, index=input.stratumType.index(session.get('Layer3', 'Medium Sand/Gravel')))
            session.Layer4 = st.selectbox('Layer 4', input.stratumType, index=input.stratumType.index(session.get('Layer4', 'Very Stiff Clay')))
        with col2:
            session.stratumThicknessL1 = st.text_input('Thickness L1', session.get('stratumThicknessL1', '6'))
            session.stratumThicknessL2 = st.text_input('Thickness L2', session.get('stratumThicknessL2', '6'))
            session.stratumThicknessL3 = st.text_input('Thickness L3', session.get('stratumThicknessL3', '30'))
            session.stratumThicknessL4 = st.text_input('Thickness L4', session.get('stratumThicknessL4', '6'))
            
        session.averageSurfaceLevel = st.text_input('Average Surface level', session.get('averageSurfaceLevel', '5'))