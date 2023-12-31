import streamlit as st
from tools import graph_maker
from tools import sidebar_module
from PIL import Image


def execute():

    session = st.session_state
    
    with open( "Styling/styles.css" ) as css:
        st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)
        
        
    col1, col2 = st.columns([0.1,0.9])
    # col1:
        #imageecozero  = Image.open('images/EcoZero.JPG')
        #resized_image = imageecozero.resize((150, 150))
        #st.image(resized_image)
    with col2:
        st.markdown("<h1>RC Column - Calculations</h1>", unsafe_allow_html=True)
    #st.image('MV5BNzlhYjEzOGItN2MwNS00ODRiLWE5OTItYThiNmJlMTdmMzgxXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_.jpg')
    st.divider()

    # Create an instance of the SidebarInputs class
    sidebar_module.sidebar_inputs()
    
    st.write(session.gridXarray)

execute()