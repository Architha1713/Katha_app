import streamlit as st

# Page Configuration
st.set_page_config(
    page_title="Katha",
    page_icon="icon.png",  # Keep icon.png in same folder (or change to 🌸 if no image yet)
    layout="wide"
)

# 🌿 PREMIUM ANIMATED UI CSS
st.markdown("""
<style>

/* Animated Gradient Background */
.stApp {
    background: linear-gradient(-45deg, #F6FFF4, #E8FAD9, #D4F4B2, #B7E892);
    background-size: 400% 400%;
    animation: gradientBG 15s ease infinite;
}

/* Gradient Animation */
@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* Floating Glow Particles */
.glow {
    position: fixed;
    width: 200px;
    height: 200px;
    background: radial-gradient(circle, rgba(183,232,146,0.4) 0%, rgba(183,232,146,0) 70%);
    border-radius: 50%;
    animation: float 12s infinite ease-in-out;
    z-index: 0;
}

.glow:nth-child(1) {
    top: 10%;
    left: 5%;
}

.glow:nth-child(2) {
    top: 60%;
    left: 80%;
    animation-delay: 4s;
}

.glow:nth-child(3) {
    top: 80%;
    left: 20%;
    animation-delay: 8s;
}

/* Floating Animation */
@keyframes float {
    0% {transform: translateY(0px);}
    50% {transform: translateY(-30px);}
    100% {transform: translateY(0px);}
}

/* Main Title Styling */
.main-title {
    font-size: 78px;
    font-weight: 900;
    text-align: center;
    color: #1B5E20;
    letter-spacing: 3px;
    font-family: 'Segoe UI', sans-serif;
    animation: fadeIn 2s ease-in-out;
}

/* Subtitle */
.subtitle {
    font-size: 26px;
    text-align: center;
    color: #2E7D32;
    margin-top: -10px;
    animation: fadeIn 3s ease-in-out;
}

/* Feature Card */
.feature-card {
    background-color: rgba(255, 255, 255, 0.75);
    padding: 25px;
    border-radius: 20px;
    box-shadow: 0px 8px 25px rgba(0,0,0,0.08);
    backdrop-filter: blur(10px);
    transition: transform 0.3s ease;
}

.feature-card:hover {
    transform: translateY(-5px);
}

/* Fade Animation */
@keyframes fadeIn {
    0% {opacity: 0; transform: translateY(30px);}
    100% {opacity: 1; transform: translateY(0);}
}

</style>

<!-- Floating Glow Elements -->
<div class="glow"></div>
<div class="glow"></div>
<div class="glow"></div>

""", unsafe_allow_html=True)

# 🌸 HERO SECTION
st.markdown('<div class="main-title">Katha</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">A Multilingual AI Companionship & Life Stories Platform for Seniors </div>',
    unsafe_allow_html=True
)

st.write("")

# Emotional Intro
st.info("Every senior has a story. Katha is a safe, warm space to connect, share memories, and build meaningful friendships.")

st.write("---")

# 💎 PREMIUM FEATURE CARDS
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
    <h3>👵 Companionship</h3>
    <p>Connect seniors with trusted friends, volunteers, and social circles in a safe environment.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
    <h3>📖 Life Stories Vault</h3>
    <p>Preserve precious memories and life journeys digitally with dignity and emotional value.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
    <h3>🌐 Multilingual Support</h3>
    <p>Supports Kannada, Telugu, Tamil, Malayalam, Hindi, and English for inclusive communication.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("---")

# Mission Section
st.header(" Our Mission")
st.write("""
Katha is designed to reduce loneliness among seniors by creating a multilingual, AI-assisted, and emotionally intelligent platform 
where stories are heard, friendships are formed, and memories are preserved with dignity.
""")

st.caption("🌸 Katha | Connecting Hearts Through Stories")
