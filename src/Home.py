import streamlit as st
import webbrowser
import os
import templates.pricing
import templates.footer
import templates.teams
import templates.products_list
import templates.page_config
import base64

def home():
    # Define the image URL 
    image_url = 'assets/logo.png'
    image_height = 50  # in pixels
    image_width = 50  # in pixels

    # Convert the image to base64 to be used in the Markdown content
    with open(image_url, "rb") as image_file:
        image_base64 = base64.b64encode(image_file.read()).decode()

    # Create the Markdown content with aligned image
    markdown_content = f"""
    <div style="display: flex; align-items: center;">
        <img src="data:image/png;base64,{image_base64}" alt="Image" style="height: {image_height}px; width: {image_width}px; margin-right: 10px;">
        <h5>CANDILYTICS | Intelligence Candidacy Analytics</h5>
        <a href="https://vocalytics.pro" target="_self"><button style="background-color: #FF6404; color: #0E0022; border-radius: 10px; padding: 8px 16px; border: none;"><b>Access Beta Version<b>🚀</button></a>
    </div>
    """

    # Render the Markdown content in Streamlit
    st.markdown(markdown_content, unsafe_allow_html=True)

    st.markdown("---")
    #Description
    st.markdown(
        """ 
        <h5 style='text-align:center;'>CANDILYTICS is an advanced application that leverages cutting-edge technologies to provide intelligent and faster Candendacy solutions to reduce gap in between Company, Candidate, Hiring & Candidacy Interview Process .</h5>
        """,
        unsafe_allow_html=True)

    templates.products_list.products_list()
    templates.pricing.pricing_page()
    templates.teams.teams_member()
    templates.footer.footer()
    templates.page_config.pagset_page_confige_config()

if __name__ == "__main__":
    home()











