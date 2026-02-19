import streamlit as st

# Page Config (You can change icon image later)
st.set_page_config(
    page_title="Katha",
    page_icon="🌸",  # we will replace with image next
    layout="wide"
)

# 🌿 Custom CSS for Premium UI + Gradient + Animation
st.markdown("""
<style>
/* Background Gradient */
.stApp {
    background: linear-gradient(135deg, #F4FFF2, #B7E892);
}

/* Main Title Styling */
.main-title {
    font-size: 70px;
    font-weight: 800;
    text-align: center;
    color: #2E7D32;
    font-family: 'Segoe UI', sans-serif;
    letter-spacing: 2px;
    animation: fadeIn 2s ease-in;
}

/* Subtitle Styling */
.subtitle {
    font-size: 26px;
    text-align: center;
    color: #1B5E20;
    margin-top: -10px;
    animation: fadeIn 3s ease-in;
}

/* Info Box Styling */
.stInfo {
    border-radius: 15px;
    font-size: 18px;
}

/* Smooth Fade Animation */
@keyframes fadeIn {
    0% {opacity: 0; transform: translateY(20px);}
    100% {opacity: 1; transform: translateY(0);}
}
</style>
""", unsafe_allow_html=True)

# 🌸 HERO SECTION (BIG TITLE)
st.markdown('<div class="main-title">Katha</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">A Multilingual AI Companionship & Life Stories Platform for Seniors </div>',
    unsafe_allow_html=True
)

st.write("")

st.info("Every senior has a story. Katha is a safe space to connect, share memories, and build meaningful friendships.")

st.write("---")

# Feature Section
col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("### 👵 Companionship")
    st.write("Connect seniors with friends and volunteers in a safe environment.")

with col2:
    st.markdown("### 📖 Life Stories Vault")
    st.write("Preserve memories and life journeys digitally with dignity.")

with col3:
    st.markdown("### 🌐 Multilingual Support")
    st.write("Supports Kannada, Telugu, Tamil, Malayalam, Hindi, and English.")
