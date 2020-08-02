from rest_framework import serializers

from apps.weather.models import Weather


class WeatherSerializer(serializers.ModelSerializer):
    class Meta:
        model = Weather
        fields = ['name', 'weather_type', 'description', 'latitude', 'longitude', 'date_time']
