from django.urls import path
from . import views
urlpatterns = [
    path("weather/", views.WeatherAPI.as_view(), name="WeatherAPI"),
    path("weather/<str:month>/", views.WeatherMonthAPI.as_view(), name="WeatherMonthAPI"),
    path("weather/<str:year>/<str:month>/", views.WeatherYearMonthAPI.as_view(), name="WeatherYearMonthAPI"),
]
