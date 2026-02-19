import streamlit as st
import pandas as pd
import os

st.title("📖 Life Stories Vault")

os.makedirs("data", exist_ok=True)

name = st.text_input("Your Name")
story = st.text_area("Share Your Life Story")

if st.button("Save Story"):
    story_data = pd.DataFrame([[name, story]], columns=["Name", "Story"])
    file_path = "data/stories.csv"

    if os.path.exists(file_path):
        story_data.to_csv(file_path, mode="a", header=False, index=False)
    else:
        story_data.to_csv(file_path, index=False)

    st.success("Story Saved Successfully 💕")

st.subheader("📚 Saved Stories")
if os.path.exists("data/stories.csv"):
    df = pd.read_csv("data/stories.csv")
    st.write(df)
