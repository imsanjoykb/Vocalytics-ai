import streamlit as st
import os
import base64

base_url = os.environ.get('BASE_URL')
google_drive = os.environ.get('GOOGLE_DRIVE')

def products_list():
    st.markdown("---")
    st.markdown("<h2 style='text-align: center;'>Products</h2>", unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        #https://drive.google.com/file/d/1urLhuhAOMqtdPNjPg319s4s8rM1cGY72/view?usp=sharing
        if os.path.exists(os.path.join("assets", "Speech_Recognition.png")):
            st.markdown(f'''<a href="{base_url}/Speech_Recognition" target="_self"><img height=46 style="border:0px;height:95px;" src="data:image/png;base64,{get_image_base64(os.path.join('assets', 'Speech_Recognition.png'))}" border="0" alt="Resume_Scoring_with_JD" /></a>''', unsafe_allow_html=True)
        else:
            st.error("Error: Could not find 'Speech_Recognition.png' in assets folder.")
        if os.path.exists(os.path.join("assets", "Audio_Augmentation.png")):
            st.markdown(f'''<a href="{base_url}/Audio_Augmentation_Visualization" target="_self"><img height=36 style="border:0px;height:95px;" src="data:image/png;base64,{get_image_base64(os.path.join('assets', 'Audio_Augmentation.png'))}" border="0" alt="Career_Coach" /></a>''', unsafe_allow_html=True)
        else:
            st.error("Error: Could not find 'Audio_Augmentation.png' in assets folder.")
        if os.path.exists(os.path.join("assets", "Audio_Data_Analysis.png")):
            st.markdown(f'''<a href="{base_url}/Audio_Data_Analysis" target="_self"><img height=36 style="border:0px;height:95px;" src="data:image/png;base64,{get_image_base64(os.path.join('assets', 'Audio_Data_Analysis.png'))}" border="0" alt="chat with company profile" /></a>''', unsafe_allow_html=True)
        else:
            st.error("Error: Could not find 'Audio_Data_Analysis.png' in assets folder.")
        #st.markdown(f'''<a href="{base_url}/Chat_with_Company_Profile" target="_self"><img height=36 style="border:0px;height:95px;" src="{google_drive}1kgAo8sgh16jy_y4r9JuKsbKMfSLj6628" border="0" alt="Chat_with_Company_Profile" /></a>''', unsafe_allow_html=True)
    with col2:
        st.markdown(f'''<a href="{base_url}/Text_to_Speech" target="_self"><img height=36 style="border:0px;height:95px;" src="data:image/png;base64,{get_image_base64(os.path.join('assets', 'Text_to_Speech.png'))}" border="0" alt="Refine_Resume_with_JD" /></a>''', unsafe_allow_html=True)
        st.markdown(f'''<a href="{base_url}/Transcriber" target="_self"><img height=36 style="border:0px;height:95px;" src="data:image/png;base64,{get_image_base64(os.path.join('assets', 'Transcriber.png'))}" border="0" alt="Professional_Screen_Test" /></a>''', unsafe_allow_html=True)
        st.markdown(f'''<a href="{base_url}/Podcast_Summarizer" target="_self"><img height=36 style="border:0px;height:95px;" src="data:image/png;base64,{get_image_base64(os.path.join('assets', 'Podcast_Summarizer.png'))}" border="0" alt="Interview_Round_with_Expert" /></a>''', unsafe_allow_html=True)

    with col3:
        st.markdown(f'''<a href="{base_url}/Speech_to_Text" target="_self"><img height=36 style="border:0px;height:95px;" src="data:image/png;base64,{get_image_base64(os.path.join('assets', 'Speech_to_Text.png'))}" border="0" alt="Improve_Resume" /></a>''', unsafe_allow_html=True)
        st.markdown(f'''<a href="{base_url}/Meeting_Summarizer" target="_self"><img height=36 style="border:0px;height:95px;" src="data:image/png;base64,{get_image_base64(os.path.join('assets', 'Meeting_Summarizer.png'))}" border="0" alt="Behavioral_Screen_Test" /></a>''', unsafe_allow_html=True)
        st.markdown(f'''<a href="{base_url}/Dubbing_AI" target="_self"><img height=36 style="border:0px;height:95px;" src="data:image/png;base64,{get_image_base64(os.path.join('assets', 'Dubbing_AI.png'))}" border="0" alt="Interview_Preparatory_Assistant" /></a>''', unsafe_allow_html=True)

    with col4:
        st.markdown(f'''<a href="{base_url}/Youtube_Summarizer" target="_self"><img height=36 style="border:0px;height:95px;" src="data:image/png;base64,{get_image_base64(os.path.join('assets', 'Youtube_Summarizer.png'))}" border="0" alt="Cover_Letter_Generator" /></a>''', unsafe_allow_html=True)
        st.markdown(f'''<a href="{base_url}/AI_Audio_Transcriber" target="_self"><img height=36 style="border:0px;height:95px;" src="data:image/png;base64,{get_image_base64(os.path.join('assets', 'AI_Audio_Transcriber.png'))}" border="0" alt="Email_Generator_for_Job" /></a>''', unsafe_allow_html=True)
        st.markdown(f'''<a href="{base_url}/Audio_Recorder" target="_self"><img height=36 style="border:0px;height:95px;" src="data:image/png;base64,{get_image_base64(os.path.join('assets', 'Audio_Recorder.png'))}" border="0" alt="InterviewPrep_with_JD" /></a>''', unsafe_allow_html=True)

def get_image_base64(file_path):
    with open(file_path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")
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

