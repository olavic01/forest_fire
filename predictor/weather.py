import requests

API_KEY = '41cdaea41516c53f524cc9b12934f7c1'  # keep private
BASE_URL = 'https://api.openweathermap.org/data/2.5/weather'

def get_weather_data(city_name='Abuja', country_code='NG'):
    try:
        url = f"{BASE_URL}?q={city_name},{country_code}&appid={API_KEY}&units=metric"
        response = requests.get(url)
        data = response.json()

        if response.status_code != 200 or "main" not in data:
            raise Exception(data.get("message", "Failed to get weather data."))

        temp = data["main"]["temp"]
        humidity = data["main"]["humidity"]
        wind_speed = data["wind"]["speed"]
        rain = data.get("rain", {}).get("1h", 0.0)  # mm

        return {
            "temp": temp,
            "humidity": humidity,
            "wind": wind_speed,
            "rain": rain
        }

    except Exception as e:
        print("Weather API Error:", e)
        return None


