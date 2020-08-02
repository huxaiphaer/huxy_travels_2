from django.contrib import admin
from django.urls import path
from django.conf.urls import url, include
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.users.views import AuthCreateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/login/', TokenObtainPairView.as_view(), name='login_view'),
    url(r'^api/v1/tour/', include('apps.tourpackages.urls')),
    url(r'^api/v1/weather_forecast/', include('apps.weather.urls')),
    path('api/v1/auth/create/', AuthCreateView.as_view()),
]
