from django.urls import path

from apps.users.views import AuthCreateView

urlpatterns = [
    path('create', AuthCreateView.as_view())
]
