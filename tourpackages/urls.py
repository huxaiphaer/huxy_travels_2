from django.conf.urls import url

from . import views

urlpatterns =[
    url(r'^$', views.ListTourPackages.as_view(), name='tours_list')
]