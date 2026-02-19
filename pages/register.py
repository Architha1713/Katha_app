import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Register | Katha", layout="wide")

# 🌸 Same Premium CSS (Consistency)
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Dancing+Script:wght@500;700&display=swap" rel="stylesheet">

<style>
.stApp {
    background: linear-gradient(-45deg, #F7FFF2, #EAFAD7, #DFF3C3, #B7E892);
    background-size: 400% 400%;
    animation: gradientBG 18s ease infinite;
}

@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* Subtle glow */
.glow {
    position: fixed;
    width: 220px;
    height: 220px;
    background: radial-gradient(circle, rgba(183,232,146,0.18) 0%, rgba(183,232,146,0) 70%);
    border-radius: 50%;
    filter: blur(60px);
    animation: float 25s infinite ease-in-out;
    z-index: -1;
}

.glow1 { top: 15%; left: 10%; }
.glow2 { top: 70%; left: 75%; }

@keyframes float {
    0% {transform: translateY(0px);}
    50% {transform: translateY(-35px);}
    100% {transform: translateY(0px);}
}

.page-title {
    font-family: 'Playfair Display', serif;
    font-size: 55px;
    text-align: center;
    color: #2F4F2F;
}

.subtitle {
    font-family: 'Dancing Script', cursive;
    font-size: 28px;
    text-align: center;
    color: #1B5E20;
}

.form-card {
    background: rgba(255,255,255,0.75);
    padding: 30px;
    border-radius: 20px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.08);
    backdrop-filter: blur(10px);
}
</style>

<div class="glow glow1"></div>
<div class="glow glow2"></div>
""", unsafe_allow_html=True)

# 🌸 Titles
st.markdown('<div class="page-title">Join Katha</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Create your profile to begin meaningful connections 💖</div>', unsafe_allow_html=True)

st.write("")

# 💎 Form Card Container
with st.container():
    st.markdown('<div class="form-card">', unsafe_allow_html=True)

    os.makedirs("data", exist_ok=True)

    name = st.text_input("👤 Name")
    age = st.number_input("🎂 Age", 50, 100)

    language = st.selectbox(
        "🌐 Preferred Language",
        ["Kannada", "Telugu", "Tamil", "Malayalam", "Hindi", "English"]
    )

    interests = st.multiselect(
        "💖 Select Interests",
        ["Music", "Gardening", "Stories", "Walking", "Spirituality", "Cooking", "Reading"]
    )

    connection_type = st.selectbox(
        "🤝 Connection Type",
        ["Elder Friend", "Student Companion", "Community Circle"]
    )

    if st.button("✨ Register with Katha"):
        user_data = pd.DataFrame(
            [[name, age, language, str(interests), connection_type]],
            columns=["Name", "Age", "Language", "Interests", "Connection"]
        )

        file_path = "data/users.csv"

        if os.path.exists(file_path):
            user_data.to_csv(file_path, mode="a", header=False, index=False)
        else:
            user_data.to_csv(file_path, index=False)

        st.success("🎉 Registration Successful! Welcome to Katha 💖")

    st.markdown('</div>', unsafe_allow_html=True)
