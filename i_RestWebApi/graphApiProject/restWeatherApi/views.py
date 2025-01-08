from django.shortcuts import render
from rest_framework import generics

from .models import WeatherSeoul
from .serializers import WeatherSerializer
# Create your views here.
class WeatherAPI(generics.ListAPIView):
    queryset = WeatherSeoul.objects.all()
    serializer_class = WeatherSerializer

class WeatherMonthAPI(generics.ListAPIView):
    queryset = WeatherSeoul.objects.all()
    serializer_class = WeatherSerializer

    def get_queryset(self):
        return WeatherSeoul.objects.filter(month=self.kwargs["month"])
    
class WeatherYearMonthAPI(generics.ListAPIView):
    queryset = WeatherSeoul.objects.all()
    serializer_class = WeatherSerializer

    def get_queryset(self):
        return WeatherSeoul.objects.filter(year=self.kwargs["year"],
                                           month=self.kwargs["month"])