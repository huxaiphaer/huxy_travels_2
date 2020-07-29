import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'huxy_travels_2.settings')

app = Celery('huxy_travels_2')
app.config_from_object('django.conf:settings', namespace='CELERY')

app.autodiscover_tasks()
