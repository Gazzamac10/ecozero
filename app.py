import streamlit as st
import InputR

st.set_page_config(page_title="My Streamlit App", page_icon=":rocket:", layout="wide", initial_sidebar_state="expanded")


# Add custom CSS styles
st.markdown(
    """
    <style>
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



st.markdown("<h1>ECO.ZERO - Structure</h1>", unsafe_allow_html=True)
#st.image('MV5BNzlhYjEzOGItN2MwNS00ODRiLWE5OTItYThiNmJlMTdmMzgxXkEyXkFqcGdeQXVyNTAyODkwOQ@@._V1_.jpg')
st.divider()


col1, col2, col3, col4 = st.columns([0.2,0.2,0.2,0.4])
with col1:
    st.markdown("<h2>USER INPUT</h2>", unsafe_allow_html=True)
    st.markdown("<p1>Project Data</p1>", unsafe_allow_html=True)
    title = st.text_input('Project Reference', '')
    Building_Use = st.selectbox('Building Use', InputR.building_useArr)
    title = st.text_input('Country', 'UK')
    st.markdown("<p1>Geometry</p1>", unsafe_allow_html=True)
    gridXarray = st.selectbox('Grid_X', InputR.gridXArr)
    gridYarray = st.selectbox('Grid_Y', InputR.gridYArr)

with col2:
    st.markdown("<h2></h2>", unsafe_allow_html=True)
    st.markdown("<h2></h2>", unsafe_allow_html=True)
    st.markdown("<p1>Engineering Parameters</p1>", unsafe_allow_html=True)
    Piling_Meth = st.selectbox('Piling_Methodology', InputR.pileMethod)

with col3:
    st.markdown("<h2></h2>", unsafe_allow_html=True)
    st.markdown("<h2></h2>", unsafe_allow_html=True)
    st.markdown("<p1>Transfer Deck Requirements</p1>", unsafe_allow_html=True)
    Transfer_D = st.selectbox('Transfer Deck', InputR.transferDeck)
    Slab_D = st.selectbox('Slab Depth', InputR.tSlabDepth)


with col4:
    st.markdown("<h2>DESIGN STATUS CHECK</h2>", unsafe_allow_html=True)


st.divider()