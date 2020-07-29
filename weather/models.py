from django.db import models


class Weather(models.Model):
    name = models.CharField(max_length=100)
    weather_type = models.CharField(max_length=100)
    description = models.TextField()
    latitude = models.CharField(max_length=50)
    longitude = models.CharField(max_length=50)
    date_time = models.CharField(max_length=50)

    def __str__(self):
        return self.name
