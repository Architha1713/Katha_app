import streamlit as st
from utils.theme import apply_theme

st.set_page_config(
    page_title="Katha - Companionship Platform",
    layout="wide",
)

apply_theme()

# Sidebar Branding
st.sidebar.title("🌿 Katha")
st.sidebar.caption("Companionship Platform")

st.title("No Senior Should Feel *Invisible* in a Digitally Connected World")

st.markdown("""
AI-powered, multilingual, NGO-assisted companionship platform reducing loneliness among senior citizens.
""")

col1, col2 = st.columns([2, 1])

with col1:
    st.markdown("""
    <div class="card">
    <h3>Designed for Indian Urban Deployment</h3>
    <p>Katha bridges the gap between lonely seniors and compassionate volunteers using ethical AI matching and NGO-assisted onboarding.</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button("💚 Join as Volunteer"):
        st.switch_page("pages/1_Join_Katha.py")

    if st.button("👵 Register Elder via NGO"):
        st.switch_page("pages/1_Join_Katha.py")

with col2:
    st.image("https://cdn-icons-png.flaticon.com/512/3048/3048122.png", width=250)

st.markdown("""
<div class="safety-box">
🛡️ All interactions are NGO-mediated for elder safety. Contact details are shared only after verified matching.
</div>
""", unsafe_allow_html=True)