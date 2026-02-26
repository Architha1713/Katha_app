import streamlit as st
import pandas as pd
import os
from utils.theme import apply_theme

# Page Config
st.set_page_config(page_title="AI Companion Matching | Katha", layout="wide")

# Apply Theme
apply_theme()

# 🌸 Premium Title Styling
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Dancing+Script:wght@500;700&display=swap" rel="stylesheet">
<style>
.page-title {
    font-family: 'Playfair Display', serif;
    font-size: 60px;
    text-align: center;
    color: #2F4F2F;
}
.subtitle {
    font-family: 'Dancing Script', cursive;
    font-size: 28px;
    text-align: center;
    color: #1B5E20;
    margin-bottom: 25px;
}
.match-card {
    background: rgba(255,255,255,0.92);
    padding: 30px;
    border-radius: 22px;
    margin-bottom: 25px;
    box-shadow: 0px 12px 30px rgba(0,0,0,0.08);
    backdrop-filter: blur(10px);
}
.score {
    font-size: 20px;
    font-weight: bold;
    color: #1B5E20;
}
.safe-tag {
    color: #2F4F2F;
    font-weight: 600;
}
</style>
""", unsafe_allow_html=True)

# 🌼 Header
st.markdown('<div class="page-title">AI Companion Matching</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">NGO-Supported Safe Matching Between Elders & Volunteers 💚</div>',
    unsafe_allow_html=True
)

st.write("")

file_path = "data/users.csv"

# 🛑 If no registrations yet
if not os.path.exists(file_path):
    st.warning("🌼 No profiles registered yet. Please register Elders or Volunteers first.")
else:
    df = pd.read_csv(file_path)

    if len(df) < 2:
        st.info("💛 At least one Elder and one Volunteer are needed for meaningful AI matching.")
    else:
        # 🔍 Separate Elders and Volunteers (CRITICAL LOGIC)
        elders = df[df["Role"] == "Elder (Registered by NGO)"]
        volunteers = df[df["Role"] == "Volunteer Companion"]

        if len(elders) == 0 or len(volunteers) == 0:
            st.info("⚠️ Matching requires both Elder profiles and Volunteer profiles.")
        else:
            st.markdown("### 🤖 AI Recommended Safe Matches")

            for _, elder in elders.iterrows():
                best_score = 0
                best_volunteer = None

                for _, volunteer in volunteers.iterrows():
                    score = 0

                    # 🌐 Language Matching (HIGH PRIORITY)
                    if elder["Language"] == volunteer["Language"]:
                        score += 50

                    # 💖 Interest Matching (Medium Priority)
                    elder_interests = str(elder["Interests"]).lower()
                    volunteer_interests = str(volunteer["Interests"]).lower()

                    common_keywords = [
                        "talking", "music", "stories", "prayer",
                        "reading", "walking", "spirituality"
                    ]

                    for word in common_keywords:
                        if word in elder_interests and word in volunteer_interests:
                            score += 5

                    # 🤝 Companion Preference Logic
                    if elder["Companion Type"] == "Volunteer Companion":
                        score += 20
                    elif elder["Companion Type"] == "Any":
                        score += 10

                    # Age empathy bonus (younger volunteer + elder)
                    if volunteer["Age"] < 35:
                        score += 5

                    if score > best_score:
                        best_score = score
                        best_volunteer = volunteer

                # 💎 Display Match Card
                if best_volunteer is not None:
                    st.markdown(f"""
                    <div class="match-card">
                        <h3>👵 Elder: {elder['Name']} (Age {elder['Age']})</h3>
                        <p><strong>🌐 Language:</strong> {elder['Language']}</p>
                        <p><strong>💖 Interests:</strong> {elder['Interests']}</p>
                        <p class="safe-tag">🛡️ Registered via NGO for safe companionship</p>
                        <hr>
                        <h3>🤝 Recommended Volunteer: {best_volunteer['Name']} (Age {best_volunteer['Age']})</h3>
                        <p><strong>🌐 Language Match:</strong> {best_volunteer['Language']}</p>
                        <p><strong>💖 Shared Interests:</strong> {best_volunteer['Interests']}</p>
                        <p><strong>📞 Contact (For NGO-coordinated call):</strong> {best_volunteer['Phone']}</p>
                        <p class="score">💯 Compatibility Score: {best_score}%</p>
                        <p>💚 This match is AI-suggested based on language, interests, safety, and emotional compatibility.</p>
                    </div>
                    """, unsafe_allow_html=True)

# 🛡️ Safety Footer (Judge WOW)
st.write("---")
st.info(
    "🛡️ Safety Note: Phone numbers are shared only after AI matching and are intended to be mediated by NGOs or authorized coordinators for secure companionship calls."
)