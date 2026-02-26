import streamlit as st
import pandas as pd
import os
from utils.theme import apply_theme

# Page Config
st.set_page_config(page_title="Impact Dashboard | Katha", layout="wide")

# Apply Theme (animations + premium UI)
apply_theme()

# 🌸 Premium Styling
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
.impact-card {
    background: rgba(255,255,255,0.92);
    padding: 30px;
    border-radius: 22px;
    margin-bottom: 25px;
    box-shadow: 0px 12px 30px rgba(0,0,0,0.08);
    backdrop-filter: blur(10px);
}
.stat-box {
    background: rgba(183,232,146,0.25);
    padding: 25px;
    border-radius: 18px;
    text-align: center;
    font-size: 22px;
    font-weight: bold;
    color: #1B5E20;
}
</style>
""", unsafe_allow_html=True)

# 🌼 Header
st.markdown('<div class="page-title">Katha Impact Dashboard</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">Measuring Social Impact, Safety & Companionship for Seniors 💚</div>',
    unsafe_allow_html=True
)

st.write("")

# 📊 PROBLEM CONTEXT (Judges LOVE this)
st.markdown("## 👵 The Problem: Elder Loneliness in Urban India")
st.markdown("""
<div class="impact-card">
<p>In rapidly growing urban cities like Bengaluru, many senior citizens live alone due to migration of younger family members and changing lifestyles.</p>
<p>This leads to emotional isolation, reduced mental well-being, and lack of regular human interaction.</p>
<p>Despite technological growth, most elderly individuals are not digitally active, making it harder for them to access companionship platforms.</p>
</div>
""", unsafe_allow_html=True)

# 💡 SOLUTION SECTION
st.markdown("## 🤖 Our Solution: Katha")
st.markdown("""
<div class="impact-card">
<p>Katha is an AI-powered, NGO-assisted companionship platform designed specifically for senior citizens.</p>
<ul>
<li>👵 Elders are safely onboarded through NGOs and caregivers</li>
<li>🤝 Volunteers register from anywhere</li>
<li>🌐 Multilingual support for inclusive communication</li>
<li>🛡️ Safety-first matching with moderated contact sharing</li>
</ul>
</div>
""", unsafe_allow_html=True)

# 📈 LIVE IMPACT METRICS FROM APP DATA
st.markdown("## 📊 Live Platform Impact Metrics")

file_path = "data/users.csv"

if not os.path.exists(file_path):
    st.warning("No registrations yet. Impact metrics will appear after users are registered.")
else:
    df = pd.read_csv(file_path)

    total_users = len(df)
    elders = len(df[df["Role"] == "Elder (Registered by NGO)"])
    volunteers = len(df[df["Role"] == "Volunteer Companion"])

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown(f"""
        <div class="stat-box">
        👥 Total Profiles<br>{total_users}
        </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown(f"""
        <div class="stat-box">
        👵 Registered Elders<br>{elders}
        </div>
        """, unsafe_allow_html=True)

    with col3:
        st.markdown(f"""
        <div class="stat-box">
        🤝 Volunteer Companions<br>{volunteers}
        </div>
        """, unsafe_allow_html=True)

# 🛡️ SAFETY IMPACT (VERY IMPORTANT FOR JUDGES)
st.markdown("## 🛡️ Safety & Ethical Design Impact")
st.markdown("""
<div class="impact-card">
<ul>
<li>🔐 NGO-mediated elder onboarding ensures authenticity and safety</li>
<li>📞 Phone numbers shared only after verified AI matching</li>
<li>🤖 Explainable AI matching based on language, interests, and emotional compatibility</li>
<li>👨‍👩‍👧 Suitable for NGOs, hospitals, and senior care communities</li>
</ul>
</div>
""", unsafe_allow_html=True)

# 🌍 SCALABILITY (WINNING SECTION)
st.markdown("## 🌍 Scalability & Future Expansion")
st.markdown("""
<div class="impact-card">
<p>Katha can be scaled across:</p>
<ul>
<li>🏥 Hospitals & Senior Care Centers</li>
<li>🏢 Residential Welfare Associations (RWAs)</li>
<li>🤝 NGOs working with elderly communities</li>
<li>🌏 Multi-city deployment across India with multilingual support</li>
</ul>
<p><strong>Vision:</strong> No senior should feel invisible in a digitally connected world.</p>
</div>
""", unsafe_allow_html=True)