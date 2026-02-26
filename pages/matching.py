import streamlit as st
import pandas as pd
import os
from utils.theme import apply_theme

st.set_page_config(page_title="AI Matching | Katha", layout="wide")
apply_theme()

st.title("🤖 Companion Matching Dashboard")
st.subheader("Smart matching based on language, interests & emotional compatibility")

file_path = "data/users.csv"

if not os.path.exists(file_path):
    st.warning("No users registered yet. Please register first in Join Katha.")
else:
    df = pd.read_csv(file_path)

    if len(df) < 2:
        st.info("Not enough users to perform matching. Add at least 2 users.")
    else:
        st.markdown("### 💚 AI Suggested Matches")

        matches = []

        for i in range(len(df)):
            user = df.iloc[i]
            best_score = 0
            best_match = None

            for j in range(len(df)):
                if i != j:
                    other = df.iloc[j]
                    score = 0

                    # Same language = high score
                    if user["Language"] == other["Language"]:
                        score += 50

                    # Same companion preference
                    if user["Companion Type"] == other["Companion Type"]:
                        score += 30

                    # Similar interests (basic check)
                    if any(interest in str(other["Interests"]) for interest in str(user["Interests"]).split(",")):
                        score += 20

                    if score > best_score:
                        best_score = score
                        best_match = other["Name"]

            matches.append((user["Name"], best_match, best_score))

        for m in matches:
            st.markdown(f"""
            ### 👤 {m[0]}
            🤝 Best Companion Match: **{m[1]}**  
            💯 Compatibility Score: **{m[2]}%**
            """)
            st.write("---")
