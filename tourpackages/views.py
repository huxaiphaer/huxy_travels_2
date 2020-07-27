from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.authentication import JWTAuthentication

from . import models
from . import serializers


class ListTourPackages(generics.ListCreateAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
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


class Booking(generics.RetrieveUpdateDestroyAPIView):
    queryset = models.Booking.objects.all()
    serializer_class = serializers.BookingSerializer

    def put(self, request, pk):
        tour = get_object_or_404(
            models.TourPackages.objects.all(),
            pk=pk
        )

        current_capacity = tour.capacity
        tour.capacity = current_capacity -1
        tour.save()
        return Response({"message": "Booking made successfully"})
