import streamlit as st
import random

# Page Config
st.set_page_config(page_title="Coffee Date ✨", page_icon="💖", layout="centered")

# --- ULTRA COLORFUL CSS ---
st.markdown("""
    <style>
    /* Background Gradient */
    .stApp {
        background: linear-gradient(135deg, #ff9a9e 0%, #fad0c4 99%, #fad0c4 100%);
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    }
    
    /* Title Styling */
    h1 {
        color: #6d4c41 !important;
        text-shadow: 2px 2px #ffffff;
        text-align: center;
        font-size: 50px !important;
    }
    
    /* Subheader Styling */
    .stMarkdown p {
        color: #4e342e;
        font-size: 18px;
        text-align: center;
    }

    /* Button Styling */
    .stButton>button {
        width: 100%;
        border-radius: 50px;
        height: 3em;
        background-color: #d84315;
        color: white !important;
        font-weight: bold;
        border: none;
        transition: 0.3s;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    }
    
    .stButton>button:hover {
        background-color: #bf360c;
        transform: scale(1.02);
    }

    /* Input Box Styling */
    .stTextInput>div>div>input {
        border-radius: 15px;
        border: 2px solid #d84315;
    }
    </style>
    """, unsafe_allow_html=True)

# --- CONTENT ---
st.title("☕ Coffee & Chill")
st.write("### Plan your most aesthetic date yet! ✨")

# Decorative Image
st.image("https://images.unsplash.com/photo-1511920170033-f8396924c348?auto=format&fit=crop&q=80&w=500", use_container_width=True)

col1, col2 = st.columns(2)

with col1:
    name = st.text_input("Who's joining?", "Soulmate")
with col2:
    vibe = st.selectbox("Current Vibe:", ["Soft Pastel", "Neon City", "Vintage Wood", "Garden Picnic"])

# Date Logic
plans = {
    "Soft Pastel": "A flower-themed cafe with rose-petal lattes and white marble tables. 🌸",
    "Neon City": "A late-night espresso bar with glowing signs and lo-fi beats. 🌃",
    "Vintage Wood": "An old library-style cafe with the smell of books and dark roast. 📚",
    "Garden Picnic": "Grab two iced coffees and find a sunny spot under a big oak tree. 🍃"
}

if st.button("Generate Our Coffee Destiny 💖"):
    st.balloons()
    st.markdown(f"""
    <div style="background: white; padding: 20px; border-radius: 20px; border-left: 10px solid #d84315;">
        <h2 style="color: #d84315;">The Plan for {name}:</h2>
        <p style="font-size: 20px; color: #333;">{plans[vibe]}</p>
    </div>
    """, unsafe_allow_html=True)
    
    # Random Coffee Quote
    quotes = ["'Life begins after coffee.'", "'Love is in the air, and it smells like coffee.'", "'Espresso yourself!'"]
    st.write(f"*Note: {random.choice(quotes)}*")
