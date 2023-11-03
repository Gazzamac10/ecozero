import streamlit as st
from tools import graph_maker
from tools import sidebar_module

with open( "Styling/styles.css" ) as css:
    st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)
    

st.markdown("<h1>RC Column - Calculations</h1>", unsafe_allow_html=True)
#st.image('MV5BNzlhYjEzOGItN2MwNS00ODRiLWE5OTItYThiNmJlMTdmMzgxXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_.jpg')
st.divider()

# Create an instance of the SidebarInputs class
sidebar_module.sidebar_inputs()
