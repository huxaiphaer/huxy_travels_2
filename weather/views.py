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
