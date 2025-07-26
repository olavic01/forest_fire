import joblib
import numpy as np
import os
from datetime import datetime
from .get_fire_data import get_live_weather_data  # For live data from OpenWeatherMap

# Load trained model
model_path = os.path.join(os.path.dirname(__file__), '..', 'forest_fire', 'forest_fire_model.pkl')
model = joblib.load(os.path.abspath(model_path))

def predict_fire_risk(temp, RH, wind, rain, FFMC, DMC, DC, ISI):
    now = datetime.now()
    month = now.month
    day_of_week = now.weekday() + 1  # Monday=1, Sunday=7

    region_code = 1
    elevation = 350

    input_data = np.array([[temp, RH, wind, rain, month, day_of_week, FFMC, DMC, DC, ISI, region_code, elevation]])
    prediction = model.predict(input_data)[0]

    return 'High Risk 🔥' if prediction == 1 else 'Low Risk 🌲'

def predict_fire_risk_live():
    try:
        # Uses default coords inside get_live_weather_data() or hardcoded
        temp, RH, wind, rain = get_live_weather_data()
        if None in [temp, RH, wind, rain]:
            return "Error: Failed to retrieve live weather data."

        # Sample static index values (replace later if needed)
        FFMC = 85.5
        DMC = 26.2
        DC = 94.3
        ISI = 5.4

        return predict_fire_risk(temp, RH, wind, rain, FFMC, DMC, DC, ISI)
    except Exception as e:
        return f"Error: {str(e)}"

def fetch_weather_and_predict(lat, lon):
    try:
        temp, RH, wind, rain = get_live_weather_data(lat, lon)

        # Use static fire indices or enhance later
        FFMC = 85.5
        DMC = 26.2
        DC = 94.3
        ISI = 5.4

        prediction = predict_fire_risk(temp, RH, wind, rain, FFMC, DMC, DC, ISI)

        return {
            'prediction': prediction,
            'temperature': temp,
            'humidity': RH,
            'wind': wind,
            'rain': rain
        }
    except Exception as e:
        return {'error': str(e)}



import requests

def weather_forecast(request):
    # Coordinates for Abuja (can update later for other cities)
    lat = 9.05785
    lon = 7.49508

    url = f"https://api.open-meteo.com/v1/forecast?latitude={lat}&longitude={lon}&current=temperature_2m,relative_humidity_2m,wind_speed_10m,precipitation"

    try:
        response = requests.get(url)
        data = response.json()

        current = data.get("current", {})
        context = {
            'temperature': current.get('temperature_2m'),
            'humidity': current.get('relative_humidity_2m'),
            'wind_speed': current.get('wind_speed_10m'),
            'rain': current.get('precipitation'),
        }
    except Exception as e:
        context = {'error': str(e)}

    return render(request, 'weather.html', context)
