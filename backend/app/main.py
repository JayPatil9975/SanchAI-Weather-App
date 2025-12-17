from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.schemas import ChatRequest
from app.agent import ask_weather_agent

app = FastAPI(title="SanchAI Weather Assistant")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

WEATHER_KEYWORDS = [
    "weather", "temperature", "temp", "climate", "forecast",
    "rain", "hot", "cold"
]

@app.post("/chat")
def chat(request: ChatRequest):
    user_message = request.message.lower()

    print("🔥 DEBUG: request.message =", request.message)
    print("🔥 DEBUG: user_message =", user_message)

    match = any(word in user_message for word in WEATHER_KEYWORDS)
    print("🔥 DEBUG: intent_match =", match)

    if not match:
        print("❌ DEBUG: returning fallback")
        return {
            "response": "I can help only with weather-related questions. Please ask about the weather of a city."
        }

    print("✅ DEBUG: calling agent")
    response = ask_weather_agent(request.message)
    print("✅ DEBUG: agent response =", response)

    return {"response": response}
