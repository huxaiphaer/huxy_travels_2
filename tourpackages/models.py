from django.db import models

from accounts.models import User


class TourPackages(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, default='')
    price = models.FloatField()
    capacity = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Destinations(models.Model):
    tour_package = models.ForeignKey(TourPackages, related_name='destinations', on_delete=models.CASCADE, )
    location = models.CharField(max_length=255)
    tour_type = models.CharField(max_length=255)
    danger_type = models.CharField(max_length=255)


class AvailableDates(models.Model):
    date_available = models.DateField()
    tour_package = models.ForeignKey(TourPackages, related_name='available_dates', on_delete=models.CASCADE)


class Booking(models.Model):
    tour_package = models.ForeignKey(TourPackages, related_name='booking_tour', on_delete=models.CASCADE)
    user = models.ForeignKey(User, related_name='booking_user', on_delete=models.CASCADE)
