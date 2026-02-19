import streamlit as st
import pandas as pd
import os
from utils.theme import apply_theme

st.set_page_config(page_title="Join Katha", layout="wide")

# Apply Premium Global Theme (Sidebar + Background + Glow)
apply_theme()

# 🌸 Custom Fonts + Styling
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Dancing+Script:wght@500;700&display=swap" rel="stylesheet">

<style>
.page-title {
    font-family: 'Playfair Display', serif;
    font-size: 65px;
    text-align: center;
    color: #2F4F2F;
}

.subtitle {
    font-family: 'Dancing Script', cursive;
    font-size: 30px;
    text-align: center;
    color: #1B5E20;
    margin-bottom: 10px;
}

.form-card {
    background: rgba(255,255,255,0.88);
    padding: 40px;
    border-radius: 24px;
    box-shadow: 0px 12px 30px rgba(0,0,0,0.08);
    max-width: 720px;
    margin: auto;
    backdrop-filter: blur(8px);
}
</style>
""", unsafe_allow_html=True)

# 🌸 Page Title
st.markdown('<div class="page-title">Join Katha</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Create your profile for meaningful companionship 💖</div>', unsafe_allow_html=True)

st.write("")

# Ensure data folder exists
os.makedirs("data", exist_ok=True)

# 💎 Premium Form Card
st.markdown('<div class="form-card">', unsafe_allow_html=True)

name = st.text_input("👤 Name")
age = st.number_input("🎂 Age", min_value=50, max_value=100, step=1)

language = st.selectbox(
    "🌐 Preferred Language",
    ["Kannada", "Telugu", "Tamil", "Malayalam", "Hindi", "English"]
)

interests = st.multiselect(
    "💖 Interests",
    ["Talking", "Music", "Spirituality", "Walking", "Stories", "Prayer", "Reading"]
)

# 🤝 SIMPLIFIED CONNECTION TYPE (Senior-Friendly)
connection_type = st.selectbox(
    "🤝 Preferred Companion Type",
    ["Elder Friend", "Student Companion"]
)

if st.button("🌸 Join Katha"):
    user_data = pd.DataFrame(
        [[name, age, language, str(interests), connection_type]],
        columns=["Name", "Age", "Language", "Interests", "Companion Type"]
    )

    file_path = "data/users.csv"

    if os.path.exists(file_path):
        user_data.to_csv(file_path, mode="a", header=False, index=False)
    else:
        user_data.to_csv(file_path, index=False)

    st.success("🌸 Successfully joined Katha! A suitable companion will be matched soon.")

st.markdown('</div>', unsafe_allow_html=True)
