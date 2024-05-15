import streamlit as st
import webbrowser

def redirect_to_google():
    webbrowser.open_new_tab("https://calendly.com/imsanjoykb")

def pricing_page():
    st.markdown(
        """
        <style>
            .bd-placeholder-img {
                font-size: 1.125rem;
                text-anchor: middle;
                -webkit-user-select: none;
                -moz-user-select: none;
                user-select: none;
            }

            .centered-text {
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            }

            @media (min-width: 768px) {
                .bd-placeholder-img-lg {
                    font-size: 3.5rem;
                }
            }
        </style>
        """,
        unsafe_allow_html=True
    )
    st.markdown("<h2 style='text-align: center;'>Pricing</h2>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center;'>Effective pricing for potential customers.</h5>", unsafe_allow_html=True)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### Free")
        st.markdown("#### $0 /mo")
        st.markdown("- Limited access\n- Limited Customization\n- Limited AI & Analytics component\n- Email support")
        st.button("Free Access")

    with col2:
        st.markdown("### Pro")
        st.markdown("#### $35 /mo")
        st.markdown("- Unlimited Access\n- Faster response speed\n- Access all AI & Analytics features\n- Priority customer support")
        st.button("Get in Touch", on_click=redirect_to_google)

    with col3:
        st.markdown("### Enterprise")
        st.markdown("#### $185 /mo")
        st.markdown("- Access all features\n- Admin access & control\n- Compliance & Data Backup\n- Priority Email & Phone Support")
        st.button("Get in Touch.", on_click=redirect_to_google)

    st.markdown("<h3 style='text-align: center;'>Compare plans</h3>", unsafe_allow_html=True)

    table_data = [
        ["", "Free", "Pro", "Enterprise"],
        ["Public", "✓", "✓", "✓"],
        ["Private", "", "✓", "✓"],
        ["Permissions", "", "✓", "✓"],
        ["Sharing", "", "", "✓"],
        ["Unlimited members", "", "", "✓"],
        ["Extra security", "", "", "✓"]
    ]

    st.table(table_data)

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
    pricing_page()