from django.urls import path

from users.views import AuthCreateView

urlpatterns = [
    path('create', AuthCreateView.as_view())
]
