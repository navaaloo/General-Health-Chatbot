# app.py
# 🩺 Health Chatbot with Friendly Chat Bubbles + Improved Safety Filter + Gemini API

import streamlit as st
from dotenv import load_dotenv
import os
import google.generativeai as genai

# ==============================
# 🔑 Load API Key
# ==============================
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")
genai.configure(api_key=GEMINI_API_KEY)

# ==============================
# ⚙️ Streamlit Config
# ==============================
st.set_page_config(page_title="Health Chatbot", page_icon="🩺", layout="centered")
st.title("🩺 General Health Query Chatbot")
st.markdown("Ask general health questions and get friendly, safe answers!")

# ==============================
# 🗨️ Chat History
# ==============================
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# ==============================
# ⚡ Improved Safety Filter
# ==============================
# Add common medicine names + general medical terms
DANGEROUS_KEYWORDS = [
    "paracetamol", "ibuprofen", "acetaminophen", "aspirin",
    "prescription", "dose", "inject", "surgery", "diagnose", 
    "medication", "drug", "treatment plan", "tablet", "capsule"
]

def is_safe_query(user_input):
    """
    Checks if the user question contains potentially dangerous or prescription-related keywords.
    """
    user_input_lower = user_input.lower()
    for word in DANGEROUS_KEYWORDS:
        if word.lower() in user_input_lower:
            return False
    return True

# ==============================
# ⚡ Prompt Engineering + Gemini API
# ==============================
def generate_response(user_input):
    """
    Sends user input to Gemini API with prompt for friendly, safe health responses.
    """
    prompt = f"""
You are a friendly and helpful health assistant.
- Explain in simple, easy-to-understand language.
- Never give instructions to take medicine, diagnose conditions, or replace a doctor.
- If asked about medication or serious symptoms, politely tell the user to consult a healthcare professional.

User question: "{user_input}"
Friendly response:
"""
    try:
        model = genai.GenerativeModel("gemini-2.0-flash-001")  # Replace with your valid Gemini model
        response = model.generate_content(prompt)
        return response.text.strip()
    except Exception as e:
        return f"⚠️ Error: {e}"

# ==============================
# 🗨️ Chat Input
# ==============================
user_input = st.text_input("Type your question here:")

if st.button("Send") and user_input:
    if is_safe_query(user_input):
        answer = generate_response(user_input)
    else:
        answer = "⚠️ Sorry, I cannot provide answers about medications or medical procedures. Please consult a healthcare professional."
    
    st.session_state.chat_history.append({"user": user_input, "bot": answer})

# ==============================
# 🗨️ Display Chat Bubbles
# ==============================
for chat in st.session_state.chat_history:
    # User bubble (green, right-aligned)
    st.markdown(
        f"""
        <div style="background-color:#DCF8C6; padding:10px; border-radius:10px; max-width:70%; margin-bottom:5px; margin-left:auto;">
        <strong>You:</strong> {chat['user']}
        </div>
        """, unsafe_allow_html=True
    )
    # Bot bubble (grey, left-aligned)
    st.markdown(
        f"""
        <div style="background-color:#F1F0F0; padding:10px; border-radius:10px; max-width:70%; margin-bottom:15px;">
        <strong>Bot:</strong> {chat['bot']}
        </div>
        """, unsafe_allow_html=True
    )

# ==============================
# 🔄 Clear Chat Button
# ==============================
if st.button("Clear Chat"):
    st.session_state.chat_history = []
