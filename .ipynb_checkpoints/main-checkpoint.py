from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from win32con import PRINTRATEUNIT_PPM

app = FastAPI()

# Enable CORS so Streamlit can call the API
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    print("i'm working")
    message = data.get("message", "").lower().strip()
    print("i'm working 1")

    print("📨 Received:", message)

    # Basic responses
    if "sad" in message:
        reply = "🌸 I'm here for you. You're not alone – Serena 🤍"
    elif "happy" in message:
        reply = "😊 That’s great to hear! Keep the positivity going."
    elif "anxious" in message:
        reply = "🧘 I understand. Take a deep breath with me."
    elif "angry" in message:
        reply = "😔 I'm sorry you're feeling this way. Want to talk about it?"
    else:
        reply = "💬 I'm listening. Tell me more."

    return {"reply": reply}
