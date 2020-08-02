from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.WeatherView.as_view(), name='weather_forecast'),
    url(r'^search/(?P<lat>.+)/(?P<lon>.+)/$', views.WeatherViewByLocation.as_view(), name='weather_forecast'),
]
