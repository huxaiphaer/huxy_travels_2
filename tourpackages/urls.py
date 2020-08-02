from django.conf.urls import url
from django.urls import path

from . import views

urlpatterns = [
    url(r'^$', views.ListTourPackages.as_view(), name='tours_list'),
    path('booking/<int:pk>', views.Booking.as_view(), name='booking'),
    url(r'(?P<pk>\d+)/$', views.RetrieveUpdateDeleteTourPackages.as_view(), name='tour_detail'),
    url(r'(?P<first_date>\d+)/(?P<last_date>\d+)/$', views.TourPackagesByDate.as_view(), name='tour_by_date'),
    url(r'(?P<tour_pk>\d+)/destinations/$', views.ListDestinations.as_view(), name='destination_list'),
    url(r'(?P<tour_pk>\d+)/available_dates/$', views.ListAvailableDates.as_view(), name='available_dates_list')
]
