import streamlit as st
from utils.theme import apply_theme

st.set_page_config(
    page_title="Katha",
    page_icon="icon.png",
    layout="wide"
)

# Apply Global Premium Theme
apply_theme()

# 🌸 Main Title (Tradition-style)
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Dancing+Script:wght@500;700&display=swap" rel="stylesheet">

<style>
.main-title {
    font-family: 'Playfair Display', serif;
    font-size: 90px;
    font-weight: 900;
    text-align: center;
    color: #2F4F2F;
    letter-spacing: 2px;
}

.subtitle {
    font-family: 'Dancing Script', cursive;
    font-size: 34px;
    text-align: center;
    color: #1B5E20;
    margin-top: -10px;
}

.custom-info {
    background-color: #C2B280;
    color: #1B5E20;
    padding: 20px;
    border-radius: 18px;
    font-size: 20px;
    text-align: center;
    font-weight: 500;
    box-shadow: 0px 10px 25px rgba(0,0,0,0.08);
}

.feature-card {
    background: rgba(255, 255, 255, 0.75);
    padding: 30px;
    border-radius: 24px;
    backdrop-filter: blur(12px);
    box-shadow: 0px 12px 30px rgba(0,0,0,0.08);
}
</style>
""", unsafe_allow_html=True)

st.markdown('<div class="main-title">Katha</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">A Multilingual AI Companionship Platform for Seniors </div>', unsafe_allow_html=True)

st.write("")

st.markdown(
    '<div class="custom-info">Every senior has a story. Katha is a safe, warm space to build friendships, reduce loneliness, and connect through meaningful conversations.</div>',
    unsafe_allow_html=True
)

st.write("")
st.write("---")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
    <h3>👵 Elder Companionship</h3>
    <p>Connect seniors with trusted companions and friendly listeners.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
    <h3>🌐 Multilingual Support</h3>
    <p>Supports Kannada, Telugu, Tamil, Malayalam, Hindi and English.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
    <h3>🛡️ Safe & Simple</h3>
    <p>Designed with accessibility and emotional safety as the top priority.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("---")

st.header(" Our Mission")
st.write("""
Katha is designed to reduce loneliness among seniors by creating a simple, multilingual and emotionally safe companionship platform.
We focus on accessibility, dignity, and meaningful human connection rather than complex technology.
""")

st.write("---")

# 🛡️ SAFETY & TRUST SECTION
st.markdown("## 🛡️ Safety & Trust First Design")

st.markdown("""
<div class="feature-card">
<h4>🔐 Companion Verification</h4>
<p>All companions are screened and matched based on compatibility and safety guidelines to ensure respectful interactions with seniors.</p>

<h4>👵 Senior-Friendly Privacy</h4>
<p>Katha does not publicly share personal contact details. All connections are mediated safely through the platform.</p>

<h4>🧠 Ethical AI Matching</h4>
<p>Our AI matching system prioritizes emotional comfort, shared language, and interests rather than random pairing.</p>

<h4>👨‍👩‍👧 Human-Centered Moderation</h4>
<p>The platform is designed for NGOs, RWAs, and caregivers to oversee and ensure safe companionship for elders.</p>
</div>
""", unsafe_allow_html=True)

st.write("---")

# 🌐 MULTILINGUAL IMPACT SECTION
st.markdown("## 🌍 Designed for Multilingual India")

st.markdown("""
<div class="feature-card">
<p>Katha supports multiple Indian languages including Kannada, Telugu, Tamil, Malayalam, Hindi, and English.</p>
<p>This ensures seniors can communicate comfortably in their native language, reducing digital fear and increasing emotional connection.</p>
</div>
""", unsafe_allow_html=True)
