from .views import login_view, sign_up_view

from django.conf.urls import url

urlpatterns = [
    url(r'^login/$', login_view),
    url(r'^signup/$', sign_up_view),
]