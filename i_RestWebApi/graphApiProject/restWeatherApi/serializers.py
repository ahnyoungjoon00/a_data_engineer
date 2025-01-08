from rest_framework import serializers
from .models import WeatherSeoul

class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeatherSeoul
        fields = "__all__"