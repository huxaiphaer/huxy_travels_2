from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from weather.models import Weather
from weather.serializers import WeatherSerializer


class WeatherView(generics.ListCreateAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer


class WeatherViewByLocation(generics.ListCreateAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = Weather.objects.all()
    serializer_class = WeatherSerializer

    def get_queryset(self):
        latitude = self.kwargs['lat']
        longitude = self.kwargs['lon']

        return Weather.objects.filter(latitude=latitude, longitude=longitude)
