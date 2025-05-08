import streamlit as st
import requests
import pyttsx3

st.set_page_config(page_title="Serena - Mental Health Companion", page_icon="🌸", layout="centered")

st.title("💬 Meet Serena – Your Mental Health Companion")
st.markdown("Hi, I'm **Serena** 🌿 Let's talk anytime you need support.")

# Toggle voice output
voice_toggle = st.checkbox("🔈 Enable voice output", value=True)

# Text input
user_input = st.text_input("💭 How are you feeling?", placeholder="Type your message...")

# Voice output function
def speak_text(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Send to FastAPI
def get_serena_reply(message):
    try:
        response = requests.post("http://127.0.0.1:8000/chat", json={"message": message})
        return response.json().get("reply", "⚠️ Serena didn’t reply.")
    except Exception as e:
        print("❌ Error:", e)
        return "⚠️ Could not reach Serena's brain."

# On submit
if st.button("Send") and user_input.strip():
    reply = get_serena_reply(user_input)
    st.markdown(f"🌸 **Serena:** {reply}")
    if voice_toggle:
        speak_text(reply)

