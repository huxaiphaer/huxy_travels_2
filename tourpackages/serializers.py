from rest_framework import serializers

from . import models


class DestinationSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'tour_package',
            'location',
            'tour_type',
            'danger_type'
        )

        model = models.Destinations


class AvailableDates(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'date_available',
            'tour_package'
        )

        model = models.AvailableDates


class TourPackageSerializer(serializers.ModelSerializer):
    destinations = DestinationSerializer(many=True, read_only=True)
    available_dates = AvailableDates(many=True, read_only=True)

    class Meta:
        fields = (
            'id',
            'name',
            'description',
            'price',
            'destinations',
            'available_dates',
            'capacity',
            'created_at'
        )

        model = models.TourPackages
