import streamlit as st
import os

base_url = os.environ.get('BASE_URL')
google_drive = os.environ.get('GOOGLE_DRIVE')

def products_list():
    st.markdown("---")
    st.markdown("<h2 style='text-align: center;'>Products</h2>", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4) 
    with col1:
        st.markdown(f'''<a href="{base_url}/Speech_Recognition" target="_self"><img height=46 style="border:0px;height:95px;" src="{google_drive}1riJuFwgTbBmtRbK6bWxTqEMFIWZQ1Uxd" border="0" alt="Speech Recognition" /></a>''', unsafe_allow_html=True)
        st.markdown(f'''<a href="{base_url}/Audio_Augmentation_Visualization" target="_self"><img height=36 style="border:0px;height:95px;" src="{google_drive}14v2wbuwMqSWAx-yOcnZfymdz39eaqckY" border="0" alt="Audio Augumentation Visualization" /></a>''', unsafe_allow_html=True)
        st.markdown(f'''<a href="{base_url}/Audio_Data_Analysis" target="_self"><img height=36 style="border:0px;height:95px;" src="{google_drive}1nLkoGt0ifVzWH-lK2tV95g89l02Ebbt9" border="0" alt="Audio Data Analysis" /></a>''', unsafe_allow_html=True)
    with col2:
        st.markdown(f'''<a href="{base_url}/Text_to_Speech" target="_self"><img height=36 style="border:0px;height:95px;" src="{google_drive}1KP5QZhqrLR7loJ7pmOIr5jL8jhpGmwCu" border="0" alt="Text to Speech" /></a>''', unsafe_allow_html=True)
        st.markdown(f'''<a href="{base_url}/Transcriber" target="_self"><img height=36 style="border:0px;height:95px;" src="{google_drive}1steznTI31BuWs75qOce0MXGv6O-JIzmR" border="0" alt="Transcriber" /></a>''', unsafe_allow_html=True)
        st.markdown(f'''<a href="{base_url}/Podcast_Summarizer" target="_self"><img height=46 style="border:0px;height:95px;" src="{google_drive}1ooj4nEWsNaA-4RxWDMTCe6YqSQmqV2kH" border="0" alt="Podcast Summarizer" /></a>''', unsafe_allow_html=True)

    with col3:
        st.markdown(f'''<a href="{base_url}/Speech_to_Text" target="_self"><img height=36 style="border:0px;height:95px;" src="{google_drive}1juA6qAkUDUAg9GayISblMinZFqOkbIdp" border="0" alt="Speech to Text" /></a>''', unsafe_allow_html=True)
        st.markdown(f'''<a href="{base_url}/Meeting_Summarizer" target="_self"><img height=46 style="border:0px;height:95px;" src="{google_drive}1nfVZEdmPxIK4uMST-D3m5c_YTsoX2tti" border="0" alt="Meeting Summarizer" /></a>''', unsafe_allow_html=True)
        st.markdown(f'''<a href="{base_url}/Dubbing_AI" target="_self"><img height=36 style="border:0px;height:95px;" src="{google_drive}1iIgKzDMmVW253zYlUgsfBqqezUzdFhTL" border="0" alt="Dubbing AI" /></a>''', unsafe_allow_html=True)
        
    with col4:
        st.markdown(f'''<a href="{base_url}/Youtube_Summarizer" target="_self"><img height=46 style="border:0px;height:95px;" src="{google_drive}16FLTR-fFHS2z40enQ-SaWCLRbAiNBBa4" border="0" alt="Youtube Summarizer" /></a>''', unsafe_allow_html=True)
        st.markdown(f'''<a href="{base_url}/AI_Audio_Transcriber" target="_self"><img height=36 style="border:0px;height:95px;" src="{google_drive}1-jgT3N-19Q9Ixpnvs0-ibCK59drLQ-qR" border="0" alt="AI Audio Transcriber" /></a>''', unsafe_allow_html=True)
        st.markdown(f'''<a href="{base_url}/Audio_Recorder" target="_self"><img height=36 style="border:0px;height:95px;" src="{google_drive}1Tl0C5X_x3iG-e9dO_nOigaO9UfneQQtI" border="0" alt="Audio Recorder" /></a>''', unsafe_allow_html=True)

    st.markdown("---")

## Remove "Made with streamlit"
hide_streamlit_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

if __name__ == "__main__":
    products_list()
