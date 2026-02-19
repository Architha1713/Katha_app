import streamlit as st

st.set_page_config(
    page_title="Katha",
    page_icon="icon.png",  # change to icon.png later if needed
    layout="wide"
)

# 🎨 CUSTOM FONTS + PREMIUM UI CSS
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Dancing+Script:wght@500;700&display=swap" rel="stylesheet">

<style>

/* 🌿 Soft Animated Gradient Background */
.stApp {
    background: linear-gradient(-45deg, #F7FFF2, #EAFAD7, #DFF3C3, #B7E892);
    background-size: 400% 400%;
    animation: gradientBG 18s ease infinite;
}

/* Smooth Gradient Motion */
@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* ✨ VERY SUBTLE FLOATING GLOW (barely visible premium effect) */
.glow {
    position: fixed;
    width: 250px;
    height: 250px;
    background: radial-gradient(circle, rgba(183,232,146,0.18) 0%, rgba(183,232,146,0) 70%);
    border-radius: 50%;
    filter: blur(60px);
    animation: float 25s infinite ease-in-out;
    z-index: -1;
    opacity: 0.6;
}

.glow1 { top: 10%; left: 5%; }
.glow2 { top: 60%; left: 75%; animation-delay: 8s; }
.glow3 { top: 80%; left: 25%; animation-delay: 16s; }

@keyframes float {
    0% {transform: translateY(0px);}
    50% {transform: translateY(-40px);}
    100% {transform: translateY(0px);}
}

/* 🌸 MAIN TITLE (Tradition-style elegant serif) */
.main-title {
    font-family: 'Playfair Display', serif;
    font-size: 80px;
    font-weight: 900;
    text-align: center;
    color: #2F4F2F;
    letter-spacing: 2px;
    margin-bottom: 0px;
}

/* ✨ SUBTITLE (Script-style elegant font) */
.subtitle {
    font-family: 'Dancing Script', cursive;
    font-size: 32px;
    text-align: center;
    color: #1B5E20;
    margin-top: -10px;
}

/* 📦 CUSTOM INFO BOX (Beige #C2B280 + Green Text) */
.custom-info {
    background-color: #C2B280;
    color: #1B5E20;
    padding: 18px;
    border-radius: 14px;
    font-size: 18px;
    text-align: center;
    font-weight: 500;
    box-shadow: 0px 6px 18px rgba(0,0,0,0.08);
}

/* 💎 Glass Feature Cards */
.feature-card {
    background: rgba(255, 255, 255, 0.65);
    padding: 25px;
    border-radius: 20px;
    backdrop-filter: blur(10px);
    box-shadow: 0px 10px 30px rgba(0,0,0,0.08);
    transition: transform 0.3s ease;
}

.feature-card:hover {
    transform: translateY(-6px);
}

</style>

<!-- Subtle Floating Glow Elements -->
<div class="glow glow1"></div>
<div class="glow glow2"></div>
<div class="glow glow3"></div>

""", unsafe_allow_html=True)

# 🌸 HERO SECTION
st.markdown('<div class="main-title">Katha</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="subtitle">A Multilingual AI Companionship & Life Stories Platform for Seniors</div>',
    unsafe_allow_html=True
)

st.write("")

# 📦 CUSTOM INFO BOX (Your requested color change)
st.markdown(
    '<div class="custom-info">Every senior has a story. Katha is a safe, warm space to connect, share memories, and build meaningful friendships.</div>',
    unsafe_allow_html=True
)

st.write("")
st.write("---")

# 💎 PREMIUM FEATURE CARDS
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
    <h3>👵 Companionship</h3>
    <p>Connect seniors with trusted friends and companions in a safe emotional environment.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
    <h3>📖 Life Stories Vault</h3>
    <p>Preserve life journeys, memories, and personal stories digitally with dignity.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
    <h3>🌐 Multilingual Support</h3>
    <p>Supports Kannada, Telugu, Tamil, Malayalam, Hindi, and English for inclusive access.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("---")

st.header("Our Mission")
st.write("""
Katha is designed to reduce loneliness among seniors by creating a multilingual, emotionally intelligent,
and safe companionship platform where stories are heard, friendships are formed, and memories are preserved with dignity.
""")

st.caption("🌸 Katha | Connecting Hearts Through Stories")
