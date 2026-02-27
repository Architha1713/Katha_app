import streamlit as st

def apply_theme():
    st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;900&family=Dancing+Script:wght@500;700&display=swap" rel="stylesheet">

    <style>
    /* 🌿 Animated Gradient Background */
    .stApp {
        background: linear-gradient(-45deg, #F7FFF2, #EAFAD7, #DFF3C3, #B7E892);
        background-size: 400% 400%;
        animation: gradientBG 18s ease infinite;
        font-family: 'Playfair Display', serif;
    }

    @keyframes gradientBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    /* ✨ Floating Glow Particles (More Premium) */
    .glow {
        position: fixed;
        width: 260px;
        height: 260px;
        background: radial-gradient(circle, rgba(183,232,146,0.18) 0%, rgba(183,232,146,0) 70%);
        border-radius: 50%;
        filter: blur(70px);
        animation: float 28s infinite ease-in-out;
        z-index: -1;
        opacity: 0.45;
    }

    .glow1 { top: 10%; left: 6%; }
    .glow2 { top: 70%; left: 85%; animation-delay: 8s; }
    .glow3 { top: 40%; left: 45%; animation-delay: 15s; }

    @keyframes float {
        0% {transform: translateY(0px) translateX(0px);}
        50% {transform: translateY(-30px) translateX(10px);}
        100% {transform: translateY(0px) translateX(0px);}
    }

    /* 🌟 Soft Title Glow Pulse (Luxury Effect) */
    .main-title {
        animation: softGlow 4s ease-in-out infinite alternate;
    }

    @keyframes softGlow {
        from { text-shadow: 0 0 5px rgba(183,232,146,0.2); }
        to { text-shadow: 0 0 18px rgba(183,232,146,0.6); }
    }

    /* 💎 Card Hover Animation (Modern Premium UI) */
    .feature-card {
        transition: transform 0.3s ease, box-shadow 0.3s ease;
    }

    .feature-card:hover {
        transform: translateY(-6px);
        box-shadow: 0px 20px 40px rgba(0,0,0,0.12);
    }

    /* 🌸 Premium Sidebar */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #EAFAD7, #CFEFA9);
        border-right: 2px solid rgba(0,0,0,0.05);
    }

    /* Hide default "app" label */
    [data-testid="stSidebarNav"] > div:first-child {
        display: none;
    }

    /* Classy Sidebar Font */
    [data-testid="stSidebarNav"] li div {
        font-family: 'Playfair Display', serif !important;
        font-size: 19px;
        font-weight: 600;
        border-radius: 14px;
        padding: 12px;
        color: #1B5E20;
        letter-spacing: 0.5px;
    }

    [data-testid="stSidebarNav"] li div:hover {
        background-color: rgba(183,232,146,0.45);
        transform: translateX(4px);
        transition: 0.2s ease;
    }

    .sidebar-title {
        font-family: 'Playfair Display', serif;
        font-size: 36px;
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
    </style>

    <div class="glow glow1"></div>
    <div class="glow glow2"></div>
    <div class="glow glow3"></div>
    """, unsafe_allow_html=True)

    st.sidebar.markdown(
        """
        <div class="sidebar-title">Katha</div>
        <div class="sidebar-sub">Companionship with Dignity</div>
        """,
        unsafe_allow_html=True
    )
