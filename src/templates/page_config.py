import streamlit as st

def pagset_page_confige_config():

    #Button Design 
    m = st.markdown("""
    <style> 
    div.stButton > button:first-child {
        background-color: #54006B;
        color:#FFF8E1;
        justify-content: center;
        align-items: center;
        text-align: center;
        border-radius:6px;
    }
    </style>""", unsafe_allow_html=True)

    ## Remove "Made with streamlit"
    hide_streamlit_style = """
                <style>
                #MainMenu {visibility: hidden;}
                footer {visibility: hidden;}
                </style>
                """
    st.markdown(hide_streamlit_style, unsafe_allow_html=True)

if __name__ == "__main__":
    pagset_page_confige_config()