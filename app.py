import streamlit as st

# Page Config
st.set_page_config(
    page_title="Katha 🌸",
    page_icon="🌸",
    layout="wide"
)

# Custom CSS for Beautiful UI
st.markdown("""
    <style>
    .main {
        background-color: #FFF7F5;
    }
    .title {
        font-size: 50px;
        font-weight: bold;
        color: #C2185B;
        text-align: center;
    }
    .subtitle {
        font-size: 22px;
        text-align: center;
        color: #6A1B9A;
    }
    .feature-box {
        background-color: #FFFFFF;
        padding: 20px;
        border-radius: 15px;
        box-shadow: 2px 2px 10px rgba(0,0,0,0.1);
        margin: 10px;
    }
    </style>
""", unsafe_allow_html=True)

# Hero Section
st.markdown('<p class="title">🌸 Katha</p>', unsafe_allow_html=True)
st.markdown(
    '<p class="subtitle">A Multilingual AI Companionship & Life Stories Platform for Seniors 💖</p>',
    unsafe_allow_html=True
)

st.write("")

# Emotional Intro
st.info("Every senior has a story. Katha is a safe space to connect, share memories, and build meaningful friendships.")

st.write("---")

# Feature Section (Beautiful Columns)
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-box">
    <h3>👵👴 Companionship</h3>
    <p>Connect seniors with friends, volunteers, and community circles.</p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-box">
    <h3>📖 Life Stories Vault</h3>
    <p>Preserve memories, experiences, and life journeys digitally.</p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-box">
    <h3>🌐 Multilingual Support</h3>
    <p>Supports Kannada, Telugu, Tamil, Malayalam, Hindi, and English.</p>
    </div>
    """, unsafe_allow_html=True)

st.write("---")

# Mission Section
st.header("💝 Our Mission")
st.write("""
Katha is designed to reduce loneliness among seniors by creating a safe, multilingual, and emotionally intelligent platform where stories are heard, friendships are formed, and memories are preserved with dignity.
""")

# Footer
st.write("---")
st.caption("🌸 Katha | Connecting Hearts Through Stories")
