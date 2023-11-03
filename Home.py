import streamlit as st
import InputR
import numpy as np
from PIL import Image
import pandas as pd
from DatabaseImport import databaseSL
from Calculations import rcColumnDesignSL
from tools import graph_maker
from tools import sidebar_module # Import your sidebar module
from tools import input


def main():
    st.set_page_config(page_title="Gaz.Database-Structure", page_icon=":rocket:", layout="wide", initial_sidebar_state="expanded")

    with open( "Styling/styles.css" ) as css:
        st.markdown( f'<style>{css.read()}</style>' , unsafe_allow_html= True)

    col1, col2, col3 = st.columns([0.1,0.05,0.85])
    with col1:
        imageecozero  = Image.open('images/EcoZero.jpg')
        resized_image = imageecozero.resize((200, 200))
        st.image(resized_image)
    with col3:
        st.markdown("<h1>Eco.Zero - Structure</h1>", unsafe_allow_html=True)

    st.divider()

    # Create an instance of the SidebarInputs class
    s = sidebar_module
    s.sidebar_inputs()

    db1 = databaseSL.SummaryTable(session.gridXarray,session.gridYarray,session.Building_Use,input.facadeType,float(session.floorToCeiling),input.designTypology)

    st.write(db1)
    db1 = db1.reset_index()
    db1 = db1.rename(columns={'index': 'Typology'})


    graph1 = graph_maker.plotlyBar(db1, 'Typology', 'CornerColumn_Gk_kN')
    graph1.update_layout(height=500)

    col1, col2 = st.columns([0.7,0.3])
    with col1:
        st.plotly_chart(graph1, use_container_width=True)


if __name__ == "__main__":
    session = st.session_state
    main()