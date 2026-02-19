import streamlit as st
import pandas as pd
import os

st.title("👤 User Registration")

# Ensure data folder exists
os.makedirs("data", exist_ok=True)

name = st.text_input("Name")
age = st.number_input("Age", 50, 100)

language = st.selectbox(
    "Preferred Language",
    ["Kannada", "Telugu", "Tamil", "Malayalam", "Hindi", "English"]
)

interests = st.multiselect(
    "Select Interests",
    ["Music", "Gardening", "Stories", "Walking", "Spirituality", "Cooking"]
)

connection_type = st.selectbox(
    "Connection Type",
    ["Elder Friend", "Student Companion"]
)

if st.button("Register"):
    user_data = pd.DataFrame([[name, age, language, interests, connection_type]],
                             columns=["Name", "Age", "Language", "Interests", "Connection"])

    file_path = "data/users.csv"

    if os.path.exists(file_path):
        user_data.to_csv(file_path, mode="a", header=False, index=False)
    else:
        user_data.to_csv(file_path, index=False)

    st.success("Registered Successfully 💖")
