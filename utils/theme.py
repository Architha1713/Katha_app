import streamlit as st

def apply_theme():
    st.markdown("""
    <style>
    /* Main Background */
    .stApp {
        background: linear-gradient(180deg, #f5f8f4 0%, #eef5ec 100%);
        font-family: 'Playfair Display', serif;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background-color: #f0f5ef;
        border-right: 1px solid #e0e8df;
    }

    /* Headings */
    h1, h2, h3 {
        color: #1f2d1f;
        font-weight: 600;
    }

    /* Glass Cards */
    .card {
        background: white;
        padding: 25px;
        border-radius: 16px;
        box-shadow: 0px 6px 20px rgba(0,0,0,0.05);
        margin-bottom: 20px;
    }

    /* Buttons */
    .stButton>button {
        background-color: #8BCB7D;
        color: white;
        border-radius: 10px;
        padding: 10px 24px;
        border: none;
        font-weight: 500;
    }

    .stButton>button:hover {
        background-color: #6fb863;
        transition: 0.3s;
    }

    /* Metric Cards */
    [data-testid="metric-container"] {
        background: white;
        border-radius: 14px;
        padding: 15px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.04);
    }

    /* Safety Badge */
    .safety-box {
        background: #f3f8f2;
        padding: 15px;
        border-radius: 12px;
        border-left: 4px solid #8BCB7D;
        margin-top: 15px;
    }
    </style>
    """, unsafe_allow_html=True)