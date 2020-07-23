from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.ListTourPackages.as_view(), name='tours_list'),
    url(r'(?P<pk>\d+)/$', views.RetrieveUpdateDeleteTourPackages.as_view(), name='tour_detail'),
    url(r'(?P<tour_pk>\d+)/destinations/$', views.ListDestinations.as_view(), name='destination_list'),
    url(r'(?P<tour_pk>\d+)/available_dates/$', views.ListAvailableDates.as_view(), name='available_dates_list')
]
