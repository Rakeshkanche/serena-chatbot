# app.py
import streamlit as st
import requests
import pyttsx3

st.set_page_config(page_title="Serena - Mental Health Companion", page_icon="🌸", layout="centered")

st.title("💬 Meet Serena – Your Mental Health Companion")
st.markdown("Hi, I'm **Serena** 🌿 Just type how you feel and I'll be here for you.")

# Toggle voice output
voice_toggle = st.checkbox("🔊 Enable voice output", value=True)

# Voice engine
engine = pyttsx3.init()
def speak_text(text):
    engine.say(text)
    engine.runAndWait()

# Function to send message to backend
def get_serena_reply(message):
    try:
        response = requests.post("http://127.0.0.1:8000/chat", json={"message": message})
        return response.json().get("reply", "⚠️ Serena didn’t reply.")
    except Exception as e:
        return "⚠️ Could not reach Serena's brain."

# User message input
user_input = st.text_input("💭 How are you feeling?", placeholder="Type your thoughts here...")

if st.button("Send") and user_input.strip():
    reply = get_serena_reply(user_input)
    st.markdown(f"🌸 **Serena:** {reply}")
    if voice_toggle:
        speak_text(reply)

