
import requests

# Replace with your actual OpenWeatherMap API key
API_KEY = '3a0d651d88msh4f90e4ae5cfc0e2p1fbe66jsn52e8823a9671'

def get_live_weather_data(lat=6.5244, lon=3.3792):
    url = (
        f"https://api.openweathermap.org/data/2.5/weather?"
        f"lat={lat}&lon={lon}&appid={API_KEY}&units=metric"
    )

    response = requests.get(url)
    if response.status_code != 200:
        raise Exception("Failed to fetch weather data")

    data = response.json()

    temp = data["main"]["temp"]
    RH = data["main"]["humidity"]
    wind = data["wind"]["speed"]
    rain = data.get("rain", {}).get("1h", 0.0)  # fallback to 0 if not present

    return temp, RH, wind, rain
