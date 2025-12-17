import requests
from langchain.tools import tool
from app.config import WEATHER_API_KEY

@tool
def get_weather(city: str) -> str:
    """
    Get current weather for a given city
    """
    url = (
        "https://api.openweathermap.org/data/2.5/weather"
        f"?q={city}&appid={WEATHER_API_KEY}&units=metric"
    )

    response = requests.get(url).json()

    if response.get("cod") != 200:
        return "Sorry, I could not find weather data for that city."

    temp = response["main"]["temp"]
    description = response["weather"][0]["description"]

    return f"It is {temp}°C with {description} in {city}."
