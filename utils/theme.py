import streamlit as st

def apply_theme():
    st.markdown("""
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:wght@600;700;900&family=Dancing+Script:wght@500;700&display=swap" rel="stylesheet">

    <style>
    /* 🌿 Animated Background */
    .stApp {
        background: linear-gradient(-45deg, #F7FFF2, #EAFAD7, #DFF3C3, #B7E892);
        background-size: 400% 400%;
        animation: gradientBG 20s ease infinite;
        font-family: 'Playfair Display', serif;
    }

    @keyframes gradientBG {
        0% {background-position: 0% 50%;}
        50% {background-position: 100% 50%;}
        100% {background-position: 0% 50%;}
    }

    /* ✨ Subtle Floating Glow */
    .glow {
        position: fixed;
        width: 260px;
        height: 260px;
        background: radial-gradient(circle, rgba(183,232,146,0.18) 0%, rgba(183,232,146,0) 70%);
        border-radius: 50%;
        filter: blur(70px);
        animation: float 30s infinite ease-in-out;
        z-index: -1;
        opacity: 0.5;
    }

    .glow1 { top: 12%; left: 6%; }
    .glow2 { top: 70%; left: 80%; animation-delay: 12s; }

    @keyframes float {
        0% {transform: translateY(0px);}
        50% {transform: translateY(-35px);}
        100% {transform: translateY(0px);}
    }

    /* 🌸 PREMIUM SIDEBAR */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #EAFAD7, #CFEFA9);
        border-right: 2px solid rgba(0,0,0,0.05);
    }

    /* Hide default "app" label */
    [data-testid="stSidebarNav"] > div:first-child {
        display: none;
    }

    /* Sidebar menu font (CLASSY) */
    [data-testid="stSidebarNav"] li div {
        font-family: 'Playfair Display', serif !important;
        font-size: 19px;
        font-weight: 600;
        border-radius: 14px;
        padding: 12px;
        color: #1B5E20;
        letter-spacing: 0.5px;
    }

    /* Hover effect */
    [data-testid="stSidebarNav"] li div:hover {
        background-color: rgba(183,232,146,0.45);
        border-radius: 14px;
        transform: translateX(3px);
        transition: 0.2s ease;
    }

    /* 🌼 Sidebar Brand Title */
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
    """, unsafe_allow_html=True)

    st.sidebar.markdown(
        """
        <div class="sidebar-title">Katha</div>
        <div class="sidebar-sub">Companionship with Dignity</div>
        """,
        unsafe_allow_html=True
    )
