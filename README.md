# 🩺 General Health Query Chatbot

A friendly and safe health chatbot built with **Streamlit** and **Google Gemini API**.  
This app answers general health questions while **blocking potentially dangerous medical advice** (e.g., medication, prescriptions, treatments).

---

## **Features**

- 🤖 **Friendly and informative responses** for general health questions  
- ⚠️ **Safety filter** prevents responses about medications, doses, or medical procedures  
- 💬 **Interactive chat interface** with left/right chat bubbles  
- 🔒 **Secure API key handling** using `.env` file  
- 🧪 Built for **testing prompt engineering** and conversational AI

---

## **Demo Example Questions**

- “What causes a sore throat?”  
- “How can I improve sleep naturally?”  
- “Are there exercises for back pain?”  
- **Blocked by safety filter:** “Is paracetamol safe for children?”  

---

## **Installation**

1. Clone the repository:

```bash
git clone <your-repo-url>
cd health_chatbot

Install dependencies:
pip install -r requirements.txt

Create a .env file in the project root:

GEMINI_API_KEY=YOUR_GEMINI_API_KEY_HERE

Usage
Run the Streamlit app:
streamlit run app.py


Type your health-related question in the input box.
Press Send to get a response.
Press Clear Chat to reset the conversation.

Safety Notes
The chatbot does NOT provide real medical advice.
Always consult a healthcare professional for any health concerns, medications, or treatments.
Safety filters prevent the bot from answering questions about medications, prescriptions, or procedures.

Dependencies
Python 3.10+
Streamlit
python-dotenv
google-generativeai

Future Improvements
Add emojis and typing animations for a more interactive experience
Integrate verified medical sources for general information
Enhance UI styling with custom CSS for mobile-friendly look

Author: Nawal Shahid
