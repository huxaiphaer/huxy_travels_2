import time
from datetime import datetime

import requests as req
from celery.schedules import crontab
from celery.task import periodic_task

from apps.weather.models import Weather
from apps.weather.weather_url import cities_url, base_url, weather_api_key


@periodic_task(
    run_every=(crontab(minute='*/20')),
    name="make_weather_request",
    ignore_result=True
)
def make_weather_request():
    """
    Make request to the url
    """

    """first clear table"""
    Weather.objects.all().delete()

    city_res = req.get(cities_url)

    for i in city_res.json():
        lat = i['coord']['lat']
        lon = i['coord']['lon']
        name = i['name']

        res = req.get(
            'https://{url}?lat={lat}&lon={lon}&appid={api_key}'.format(url=base_url, lat=lat, lon=lon,
                                                                       api_key=weather_api_key))
        for i in res.json()['list']:
            weather_type = i['weather'][0]['main']
            date_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(int(i['dt'])))
            date_time_obj = datetime.strptime(date_time, '%Y-%m-%d %H:%M:%S')
            description = i['weather'][0]['description']

            Weather.objects.create(
                name=name,
                weather_type=weather_type,
                description=description,
                latitude=lat,
                longitude=lon,
                date_time=date_time_obj
            )
