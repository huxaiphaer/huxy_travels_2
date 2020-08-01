import json

from django.contrib.auth.models import User
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from weather.models import Weather
from weather.test_weather_data import TestWeatherData


class Test(TestCase, TestWeatherData):
    def setUp(self):
        """
        set up tests
        """
        User.objects.all().delete()
        Weather.objects.all().delete()

        self.login_data = {
            "username": self.user_name,
            "password": self.password
        }

        self.user_data = {
            "username": self.user_name,
            "email": self.user_email,
            "first_name": self.first_name,
            "last_name": self.last_name,
            "password": self.password
        }

        self.client = APIClient()

        self.response = self.client.post(
            "/api/v1/auth/create/",
            self.user_data,
            format="json"
        )
        self.user = User.objects.get(email=self.user_email)
        self.user.save()

        self.response = self.client.post(
            "/api/v1/login/",
            self.login_data,
            format="json")
        self.assertEqual(status.HTTP_200_OK, self.response.status_code)
        self.assertIn('access', self.response.data)
        token = self.response.data.get("access", None)
        self.client.credentials(HTTP_AUTHORIZATION="Bearer {0}".format(token))

    def test_post_weather_data(self):
        response = self.client.post(
            "/api/v1/weather_forecast/", data=json.dumps(
                self.post_weather_data), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIsInstance(response.json(), dict)

    def test_get_weather_data(self):
        response = self.client.get(
            "/api/v1/weather_forecast/", content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)
