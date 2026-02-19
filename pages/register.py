import streamlit as st
import pandas as pd
import os

st.set_page_config(page_title="Register | Katha")

st.title("👤 Join Katha")
st.subheader("Create your profile to start meaningful connections 💖")

os.makedirs("data", exist_ok=True)

with st.container():
    name = st.text_input("👤 Name")
    age = st.number_input("🎂 Age", 50, 100)

    language = st.selectbox(
        "🌐 Preferred Language",
        ["Kannada", "Telugu", "Tamil", "Malayalam", "Hindi", "English"]
    )

    interests = st.multiselect(
        "💖 Select Your Interests",
        ["Music", "Gardening", "Stories", "Walking", "Spirituality", "Cooking", "Reading"]
    )

    connection_type = st.selectbox(
        "🤝 How would you like to connect?",
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
