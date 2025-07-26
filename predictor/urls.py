from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),                        # Map page
    path('get-fire-data/', views.get_fire_data, name='get_fire_data'),  # AJAX data for map
    path('charts/', views.fire_charts, name='charts'),        # Charts page
    path('weather/', views.weather_forecast, name='weather'), # Weather forecast page (we'll build this next)
    path('weather/', views.weather_forecast, name='weather_forecast'),
    path('get-weather-chart-data/', views.get_chart_data, name='get_chart_data'),
    path('get-weather-forecast/', views.get_forecast, name='get_forecast'),
]
