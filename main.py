from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from textblob import TextBlob
import time

app = FastAPI()

# Enable CORS for frontend (Streamlit)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Simple memory for conversation (single user)
chat_history = []

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    message = data.get("message", "")
    chat_history.append(f"You: {message}")

    sentiment = TextBlob(message).sentiment.polarity
    if sentiment < -0.3:
        reply = "I'm here for you. Want to talk about what’s making you feel this way?"
    elif "lonely" in message.lower():
        reply = "I’m sorry you're feeling that way. I'm here with you right now. Would it help to talk more?"
    elif sentiment > 0.3:
        reply = "That's wonderful! Tell me more about what's making you feel happy."
    else:
        reply = "Thanks for sharing. Do you want to go deeper into that?"

    chat_history.append(f"Serena: {reply}")
    time.sleep(1.2)
    return {"reply": reply}

@app.get("/judge")
async def judge():
    return {"message": "Model evaluation not required in this conversational version."}


