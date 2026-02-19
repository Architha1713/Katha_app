import streamlit as st

# 🌸 PAGE CONFIG
st.set_page_config(
    page_title="Katha",
    page_icon="icon.png",  # You can change to "icon.png" later
    layout="wide"
)

# 🎨 COMPLETE PREMIUM CSS (UI + SIDEBAR + ANIMATIONS + FONTS)
st.markdown("""
<link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@700;900&family=Dancing+Script:wght@500;700&display=swap" rel="stylesheet">

<style>

/* 🌿 ANIMATED SOFT GREEN GRADIENT BACKGROUND */
.stApp {
    background: linear-gradient(-45deg, #F7FFF2, #EAFAD7, #DFF3C3, #B7E892);
    background-size: 400% 400%;
    animation: gradientBG 20s ease infinite;
}

/* Gradient Motion */
@keyframes gradientBG {
    0% {background-position: 0% 50%;}
    50% {background-position: 100% 50%;}
    100% {background-position: 0% 50%;}
}

/* ✨ VERY SUBTLE FLOATING GLOW PARTICLES */
.glow {
    position: fixed;
    width: 280px;
    height: 280px;
    background: radial-gradient(circle, rgba(183,232,146,0.22) 0%, rgba(183,232,146,0) 70%);
    border-radius: 50%;
    filter: blur(70px);
    animation: float 28s infinite ease-in-out;
    z-index: -1;
    opacity: 0.5;
}

.glow1 { top: 10%; left: 5%; }
.glow2 { top: 60%; left: 80%; animation-delay: 10s; }
.glow3 { top: 85%; left: 25%; animation-delay: 18s; }

@keyframes float {
    0% {transform: translateY(0px);}
    50% {transform: translateY(-45px);}
    100% {transform: translateY(0px);}
}

/* 🌸 PREMIUM SIDEBAR DESIGN */
section[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #EAFAD7, #CFEFA9);
    border-right: 2px solid rgba(0,0,0,0.05);
}

/* Hide default "app" label */
[data-testid="stSidebarNav"] > div:first-child {
    display: none;
}

/* Sidebar menu spacing */
[data-testid="stSidebarNav"] ul {
    gap: 10px;
}

/* Sidebar menu items */
[data-testid="stSidebarNav"] li div {
    font-size: 18px;
    font-weight: 500;
    border-radius: 14px;
    padding: 10px;
    color: #1B5E20;
}

/* Hover effect */
[data-testid="stSidebarNav"] li div:hover {
    background-color: rgba(183,232,146,0.5);
    border-radius: 14px;
}

/* 🌼 SIDEBAR BRAND TITLE */
.sidebar-title {
    font-family: 'Playfair Display', serif;
    font-size: 34px;
    font-weight: 900;
    color: #2F4F2F;
    text-align: center;
    margin-top: 10px;
}

.sidebar-sub {
    font-family: 'Dancing Script', cursive;
    font-size: 18px;
    text-align: center;
    color: #1B5E20;
    margin-bottom: 25px;
}

/* 🌸 MAIN TITLE (Tradition-style elegant) */
.main-title {
    font-family: 'Playfair Display', serif;
    font-size: 85px;
    font-weight: 900;
    text-align: center;
    color: #2F4F2F;
    letter-spacing: 2px;
    margin-bottom: 0px;
}

/* ✨ SUBTITLE (Script style) */
.subtitle {
    font-family: 'Dancing Script', cursive;
    font-size: 34px;
    text-align: center;
    color: #1B5E20;
    margin-top: -10px;
}

/* 📦 CUSTOM INFO BOX (#C2B280 beige + green text) */
.custom-info {
    background-color: #C2B280;
    color: #1B5E20;
    padding: 20px;
    border-radius: 16px;
    font-size: 19px;
    text-align: center;
    font-weight: 500;
    box-shadow: 0px 8px 22px rgba(0,0,0,0.08);
}

/* 💎 GLASS FEATURE CARDS */
.feature-card {
    background: rgba(255, 255, 255, 0.7);
    padding: 28px;
    border-radius: 22px;
    backdrop-filter: blur(12px);
    box-shadow: 0px 12px 35px rgba(0,0,0,0.08);
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

# 🌸 BRANDED SIDEBAR HEADER (PREMIUM NAVIGATION)
st.sidebar.markdown(
    """
    <div class="sidebar-title">Katha</div>
    <div class="sidebar-sub">Connecting Hearts Through Stories</div>
    """,
    unsafe_allow_html=True
)

# 🌸 HERO SECTION
st.markdown('<div class="main-title">Katha</div>', unsafe_allow_html=True)

st.markdown(
    '<div class="subtitle">A Multilingual AI Companionship & Life Stories Platform for Seniors</div>',
    unsafe_allow_html=True
)

st.write("")

# 📦 CUSTOM INFO BOX
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
    <p>Connect seniors with trusted friends, volunteers, and community circles in a safe emotional environment.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
    <h3>📖 Life Stories Vault</h3>
    <p>Preserve life journeys, memories, and personal stories digitally with dignity and emotional value.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
    <h3>🌐 Multilingual Support</h3>
    <p>Supports Kannada, Telugu, Tamil, Malayalam, Hindi, and English for inclusive and accessible interaction.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("---")

st.header("Our Mission")
st.write("""
Katha is designed to reduce loneliness among seniors by creating a multilingual, emotionally intelligent, 
and safe companionship platform where stories are heard, friendships are formed, and memories are preserved with dignity.
""")

st.caption("🌸 Katha | Connecting Hearts Through Stories")
