import streamlit as st
import pandas as pd
import os
from utils.theme import apply_theme

# Page Config
st.set_page_config(page_title="Join Katha", layout="wide")

# Apply Premium Theme
apply_theme()

# Ensure data folder exists
os.makedirs("data", exist_ok=True)
file_path = "data/users.csv"

# 🌸 Title Styling
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
    margin-bottom: 20px;
}
.form-card {
    background: rgba(255,255,255,0.92);
    padding: 40px;
    border-radius: 24px;
    box-shadow: 0px 12px 30px rgba(0,0,0,0.08);
    max-width: 750px;
    margin: auto;
    backdrop-filter: blur(10px);
}
</style>
""", unsafe_allow_html=True)

# 🌼 Header
st.markdown('<div class="page-title">Join Katha</div>', unsafe_allow_html=True)
st.markdown(
    '<div class="subtitle">NGO-assisted elder onboarding & volunteer companionship registration 💚</div>',
    unsafe_allow_html=True
)

st.write("")

# 💎 Form Card Start
st.markdown('<div class="form-card">', unsafe_allow_html=True)

# 👤 Name
name = st.text_input("👤 Full Name")

# 🧑 ROLE SELECTION
user_role = st.selectbox(
    "🧑 Profile Type",
    [
        "Elder (Registered by NGO)",
        "Volunteer Companion"
    ]
)

# 🎂 Dynamic Age Logic
if user_role == "Volunteer Companion":
    age = st.number_input(
        "🎂 Age",
        min_value=18,
        max_value=60,
        step=1,
        help="Volunteers must be 18+"
    )
else:
    age = st.number_input(
        "🎂 Age",
        min_value=50,
        max_value=100,
        step=1,
        help="Elder profiles are registered by NGOs or caregivers"
    )

# 📞 Phone
phone = st.text_input(
    "📞 Phone Number (Shared only after safe AI matching)",
    placeholder="Enter contact number"
)

# 🌐 MULTI-LANGUAGE (FIXED)
languages = st.multiselect(
    "🌐 Languages Known & Comfortable In",
    [
        "English",
        "ಕನ್ನಡ (Kannada)",
        "हिंदी (Hindi)",
        "தமிழ் (Tamil)",
        "తెలుగు (Telugu)",
        "മലയാളം (Malayalam)"
    ],
    help="Select all languages the user is comfortable speaking."
)

# 💖 Interests
interests = st.multiselect(
    "💖 Interests",
    ["Talking", "Music", "Spirituality", "Walking", "Stories", "Prayer", "Reading"]
)

# 🤝 Companion Preference
if user_role == "Elder (Registered by NGO)":
    companion_type = st.selectbox(
        "🤝 Preferred Companion Type",
        ["Volunteer Companion", "Any"]
    )
else:
    companion_type = st.selectbox(
        "🤝 Preferred Companion Type",
        ["Elder Friend", "Any"]
    )

# 🛡️ Safety Note
st.info(
    "🛡️ Safety Note: Contact details are securely stored and only shared with verified matches through NGOs or authorized coordinators."
)

# 🌸 Submit Button
if st.button("🌸 Register with Katha"):
    
    # Validation
    if name.strip() == "" or phone.strip() == "":
        st.error("⚠️ Please fill in all required details (Name and Phone Number).")
    
    elif len(languages) == 0:
        st.error("⚠️ Please select at least one language.")
    
    else:
        # Convert lists to clean strings
        languages_str = ", ".join(languages)
        interests_str = ", ".join(interests)

        # Create DataFrame (FIXED: languages not language)
        new_user = pd.DataFrame(
            [[name, age, phone, languages_str, interests_str, companion_type, user_role]],
            columns=[
                "Name",
                "Age",
                "Phone",
                "Languages",  # Updated column name
                "Interests",
                "Companion Type",
                "Role"
            ]
        )

        # Save to CSV safely
        if os.path.exists(file_path):
            new_user.to_csv(file_path, mode="a", header=False, index=False)
        else:
            new_user.to_csv(file_path, index=False)

        # 🌐 Multilingual Success Messages
        primary_lang = languages[0]  # First selected language

        messages = {
            "English": "🌸 Registration successful! Profile securely added for AI companionship matching.",
            "ಕನ್ನಡ (Kannada)": "🌸 ನೋಂದಣಿ ಯಶಸ್ವಿಯಾಗಿದೆ! ಪ್ರೊಫೈಲ್ ಸುರಕ್ಷಿತವಾಗಿ ಸೇರಿಸಲಾಗಿದೆ.",
            "हिंदी (Hindi)": "🌸 पंजीकरण सफल! प्रोफ़ाइल सुरक्षित रूप से जोड़ दी गई है।",
            "தமிழ் (Tamil)": "🌸 பதிவு வெற்றிகரமாக முடிந்தது! சுயவிவரம் பாதுகாப்பாக சேர்க்கப்பட்டது.",
            "తెలుగు (Telugu)": "🌸 నమోదు విజయవంతమైంది! ప్రొఫైల్ సురక్షితంగా జోడించబడింది.",
            "മലയാളം (Malayalam)": "🌸 രജിസ്ട്രേഷൻ വിജയകരമായി പൂർത്തിയായി!"
        }

        st.success(messages.get(primary_lang, messages["English"]))

# Close Form Card
st.markdown('</div>', unsafe_allow_html=True)