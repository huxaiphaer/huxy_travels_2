from rest_framework import generics

from . import models
from . import serializers


class ListTourPackages(generics.ListCreateAPIView):
    queryset = models.TourPackages.objects.all()
    serializer_class = serializers.TourPackageSerializer


class RetrieveUpdateDeleteTourPackages(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.TourPackages.objects.all()
    serializer_class = serializers.TourPackageSerializer


class ListDestinations(generics.ListCreateAPIView):
    queryset = models.Destinations.objects.all()
    serializer_class = serializers.DestinationSerializer


class RetrieveUpdateDeleteDestinations(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Destinations.objects.all()
    serializer_class = serializers.DestinationSerializer


class ListAvailableDates(generics.ListCreateAPIView):
    queryset = models.AvailableDates.objects.all()
    serializer_class = serializers.AvailableDatesSerializer


class RetrieveUpdateAvailableDates(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.AvailableDates.objects.all()
    serializer_class = serializers.AvailableDatesSerializer
