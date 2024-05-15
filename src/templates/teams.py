import streamlit as st
import webbrowser
import templates.page_config
    
def portfolio():
    webbrowser.open_new_tab("https://imsanjoykb.github.io/")
def linkedin_id():
    webbrowser.open_new_tab("https://www.linkedin.com/in/imsanjoykb/")
def instagram_id():
    webbrowser.open_new_tab("https://www.instagram.com/imsanjoykb/")

def teams_member():
    st.markdown("---")
    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("")

    with col2:
        st.markdown("### VOCALYTICS Team")
        member_picture = "assets/propic.png"
        st.image(member_picture, width=150)
        st.markdown("##### Sanjoy Kumar")
        st.markdown("Creator of VOCALYTICS\n sanjoy.eee32@gmail.com")
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.button("Pf", on_click=portfolio)
        with col2:
            st.button("in", on_click=linkedin_id)
        with col3:
            st.button("ig", on_click=instagram_id)
        with col4:
            st.markdown("")


    with col3:
        st.markdown("")

templates.page_config.pagset_page_confige_config()

if __name__ == "__main__":
    teams_member()