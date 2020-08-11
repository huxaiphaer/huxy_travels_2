from rest_framework import generics
from rest_framework.generics import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.status import HTTP_404_NOT_FOUND
from rest_framework_simplejwt.authentication import JWTAuthentication

from . import models
from . import serializers, available_serializers


class ListTourPackages(generics.ListCreateAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = models.TourPackages.objects.all()
    serializer_class = serializers.TourPackageSerializer


class TourPackagesByDate(generics.ListAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    serializer_class = available_serializers.FilterAvailableDateSerializer

    def get_queryset(self):
        print(self.request.GET)
        first_date = self.request.GET['first_date']
        last_date = self.request.GET['last_date']

        result = models.AvailableDates.objects.filter(date_available__range=[first_date, last_date])
        return result


class RetrieveUpdateDeleteTourPackages(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = models.TourPackages.objects.all()
    serializer_class = serializers.TourPackageSerializer


class ListDestinations(generics.ListCreateAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = models.Destinations.objects.all()
    serializer_class = serializers.DestinationSerializer


class RetrieveUpdateDeleteDestinations(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = models.Destinations.objects.all()
    serializer_class = serializers.DestinationSerializer


class ListAvailableDates(generics.ListCreateAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = models.AvailableDates.objects.all()
    serializer_class = serializers.AvailableDatesSerializer


class RetrieveUpdateAvailableDates(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = models.AvailableDates.objects.all()
    serializer_class = serializers.AvailableDatesSerializer


class Booking(generics.RetrieveUpdateDestroyAPIView):
    authentication_classes = (JWTAuthentication,)
    permission_classes = (IsAuthenticated,)
    queryset = models.Booking.objects.all()
    serializer_class = serializers.BookingSerializer

    def put(self, request, pk):
        tour = get_object_or_404(
            models.TourPackages.objects.all(),
            pk=pk
        )

        current_capacity = tour.capacity
        tour.capacity = current_capacity - 1

        if tour.capacity <= 0:
            return Response(status=HTTP_404_NOT_FOUND, data={"message", "Sorry, no more seats"})
        tour.save()
        return Response({"message": "Booking made successfully"})
