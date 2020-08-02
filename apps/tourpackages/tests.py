import json

from django.contrib.auth import get_user_model
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient

from apps.tourpackages.models import TourPackages
from apps.tourpackages.test_tour_packages_data import TestTourPackagesData


class Test(TestCase, TestTourPackagesData):

    def setUp(self):
        """
        set up tests
        """
        get_user_model().objects.all().delete()
        TourPackages.objects.all().delete()

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
        self.user = get_user_model().objects.get(email=self.user_email)
        self.user.save()

        self.response = self.client.post(
            "/api/v1/login/",
            self.login_data,
            format="json")
        self.assertEqual(status.HTTP_200_OK, self.response.status_code)
        self.assertIn('access', self.response.data)
        token = self.response.data.get("access", None)
        self.client.credentials(HTTP_AUTHORIZATION="Bearer {0}".format(token))

    def test_post_new_tour_package(self):
        """first post a tour package """

        response = self.client.post(
            "/api/v1/tour/", data=json.dumps(
                self.post_tour_package), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIsInstance(response.json(), dict)

        response = self.client.get(
            "/api/v1/tour/", content_type='application/json')
        self.assertEqual(response.status_code, 200)
        self.assertIsInstance(response.json(), dict)

    def test_editing_tour_package(self):
        response = self.client.post(
            "/api/v1/tour/", data=json.dumps(
                self.post_tour_package), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIsInstance(response.json(), dict)

        # Editing tour package
        response = self.client.put(
            "/api/v1/tour/{}/".format(1), data=json.dumps(
                self.updated_tour_package), content_type='application/json')

        print('--> ', response)
        self.assertEqual(response.status_code, 404)
        self.assertIsInstance(response.json(), dict)

    def test_get_single_tour_package(self):
        # Post a tour package
        response = self.client.post(
            "/api/v1/tour/", data=json.dumps(
                self.post_tour_package), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIsInstance(response.json(), dict)

        # Get single tour package
        response = self.client.get(
            "/api/v1/tour/{}/".format(1), content_type='application/json')
        self.assertEqual(response.status_code, 404)
        self.assertIsInstance(response.json(), dict)

    def test_delete_single_tour_package(self):
        # Add a tour package
        response = self.client.post(
            "/api/v1/tour/", data=json.dumps(
                self.post_tour_package), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIsInstance(response.json(), dict)

        # Delete single tour package

        response = self.client.delete(
            "/api/v1/tour/{}/".format(1))

        self.assertEqual(response.status_code, 404)

    def test_booking_tour_package(self):
        # Add a tour package
        response = self.client.post(
            "/api/v1/tour/", data=json.dumps(
                self.post_tour_package), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIsInstance(response.json(), dict)

        response = self.client.put(
            "/api/v1/tour/booking/{}".format(1)
        )

        self.assertEqual(response.status_code, 200)

    def test_capacity_of_tour_empty(self):
        # Add a tour package
        response = self.client.post(
            "/api/v1/tour/", data=json.dumps(
                self.post_tour_package), content_type='application/json')
        self.assertEqual(response.status_code, 201)
        self.assertIsInstance(response.json(), dict)

        # book once
        self.client.put(
            "/api/v1/tour/booking/{}".format(1)
        )

        # book twice
        self.client.put(
            "/api/v1/tour/booking/{}".format(1)
        )

        # book thrice
        response_two = self.client.put(
            "/api/v1/tour/booking/{}".format(1)
        )
        self.assertEqual(response_two.status_code, 404)
