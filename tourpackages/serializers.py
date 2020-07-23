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
        read_only_fields = ('tour_package',)


class AvailableDatesSerializer(serializers.ModelSerializer):
    class Meta:
        fields = (
            'id',
            'date_available',
            'tour_package'
        )

        model = models.AvailableDates
        read_only_fields = ('tour_package',)


class TourPackageSerializer(serializers.ModelSerializer):
    destinations = DestinationSerializer(many=True)
    available_dates = AvailableDatesSerializer(many=True)

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

    def create(self, validated_data):
        """
        :param validated_data:
        :return: one create tour package.
        """

        destinations_data = validated_data.pop("destinations")
        dates_data = validated_data.pop("available_dates")
        tour_package = models.TourPackages.objects.create(**validated_data)

        for dest_data in destinations_data:
            models.Destinations.objects.create(**dest_data, tour_package=tour_package)

        for dd in dates_data:
            models.AvailableDates.objects.create(**dd, tour_package=tour_package,)

        return tour_package

