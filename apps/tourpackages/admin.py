from django.contrib import admin

from apps.tourpackages import models

admin.site.register(models.TourPackages)
admin.site.register(models.AvailableDates)
admin.site.register(models.Destinations)
