from rest_framework import serializers

from . import models
from .models import Destinations, AvailableDates


class DestinationSerializer(serializers.ModelSerializer):
    id = serializers.IntegerField(required=False)

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
    id = serializers.IntegerField(required=False)

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
            models.AvailableDates.objects.create(**dd, tour_package=tour_package, )

        return tour_package

    def update(self, instance, validated_data):
        instance.name = validated_data['name']
        instance.description = validated_data['description']
        instance.price = validated_data['price']
        instance.capacity = validated_data['capacity']
        instance.save()

        # Update destinations
        for des in validated_data['destinations']:
            des_id = des.get('id', None)
            if des_id:
                destination = Destinations(id=des['id'], location=des['location'], tour_type=des['tour_type'],
                                           danger_type=des['danger_type'], tour_package=instance)
                destination.save()

        # Updating available dates
        for a_dates in validated_data['available_dates']:
            a_dates_id = a_dates.get('id', None)
            if a_dates_id:
                available_dates = AvailableDates(id=a_dates['id'], date_available=a_dates['date_available'],
                                                 tour_package=instance)
                available_dates.save()

        return instance
