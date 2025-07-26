
from django.shortcuts import render
from django.http import JsonResponse
from .utils import fetch_weather_and_predict


def home(request):
    """
    Renders the homepage containing the interactive map and prediction result.
    """
    return render(request, 'home.html')


def get_fire_data(request):
    """
    API endpoint that accepts latitude and longitude as GET parameters,
    fetches live weather, and returns fire risk prediction.
    """
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')

    if not lat or not lon:
        return JsonResponse({'error': 'Missing latitude or longitude'}, status=400)

    try:
        lat = float(lat)
        lon = float(lon)
        data = fetch_weather_and_predict(lat, lon)
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def fire_charts(request):
    return render(request, 'charts.html')

def weather_forecast(request):
    return render(request, 'weather.html')


def weather_forecast(request):
    return render(request, 'weather.html')  # We'll create this template next

def get_fire_data(request):
    lat = request.GET.get('lat')
    lon = request.GET.get('lon')
    if not lat or not lon:
        return JsonResponse({'error': 'Missing coordinates'}, status=400)
    try:
        data = fetch_weather_and_predict(float(lat), float(lon))
        return JsonResponse(data)
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)

def get_chart_data(request):
    return JsonResponse(get_mock_chart_data())  # Simulated time-series

def get_forecast(request):
    return JsonResponse(get_mock_forecast())  # Simulated daily forecast