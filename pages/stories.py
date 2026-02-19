import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Life Stories | Katha", layout="wide")

# 🌸 Same Premium Theme
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Dancing+Script:wght@500;700&display=swap" rel="stylesheet">

<style>
.stApp {
    background: linear-gradient(-45deg, #F7FFF2, #EAFAD7, #DFF3C3, #B7E892);
    background-size: 400% 400%;
    animation: gradientBG 18s ease infinite;
}

.page-title {
    font-family: 'Playfair Display', serif;
    font-size: 60px;
    text-align: center;
    color: #2F4F2F;
}

.subtitle {
    font-family: 'Dancing Script', cursive;
    font-size: 30px;
    text-align: center;
    color: #1B5E20;
}

.story-card {
    background: rgba(255,255,255,0.75);
    padding: 25px;
    border-radius: 18px;
    margin-bottom: 20px;
    box-shadow: 0px 6px 20px rgba(0,0,0,0.08);
}
</style>
""", unsafe_allow_html=True)

# 🌸 Titles
st.markdown('<div class="page-title">Life Stories Vault</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Preserve memories, experiences & life journeys 📖</div>', unsafe_allow_html=True)

st.write("")

os.makedirs("data", exist_ok=True)

# 📖 Story Input Section
st.markdown("### ✍️ Share Your Story")
name = st.text_input("Your Name")
story = st.text_area("Write your life story or memory...", height=200)

if st.button("💾 Save Story"):
    story_data = pd.DataFrame([[name, story]], columns=["Name", "Story"])
    file_path = "data/stories.csv"

    if os.path.exists(file_path):
        story_data.to_csv(file_path, mode="a", header=False, index=False)
    else:
        story_data.to_csv(file_path, index=False)

    st.success("🌸 Your story has been beautifully محفوظ in Katha!")

st.write("---")

# 📚 Display Stories (Beautiful Cards)
st.markdown("### 📚 Saved Stories")

if os.path.exists("data/stories.csv"):
    df = pd.read_csv("data/stories.csv")

    for i, row in df.iterrows():
        st.markdown(f"""
        <div class="story-card">
        <h4>🌼 {row['Name']}</h4>
        <p>{row['Story']}</p>
        </div>
        """, unsafe_allow_html=True)
