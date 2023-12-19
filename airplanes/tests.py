# airplanes/tests/test_views.py
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from .models import Airplane

class AirplaneAPITestCase(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_create_airplanes(self):
        print('test airplance fuel capacity and consumption calculation')
        data = [
            {"id": 1, "passenger_assumptions": 50},
            {"id": 2, "passenger_assumptions": 40},
        ]

        response = self.client.post('/api/airplanes/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

        self.assertIsInstance(response.data, list)
        self.assertTrue(all(isinstance(item, dict) for item in response.data))

        for item in response.data:
            self.assertIn('id', item)
            self.assertIn('passenger_assumptions', item)
            self.assertIn('fuel_consumption_per_minute', item)
            self.assertIn('max_flight_minutes', item)

    def test_create_more_than_10_airplanes(self):
        print('test more than 10 airplance triggers bad request response')
        data = [
            {"id": i, "passenger_assumptions": 50} for i in range(1, 12)
        ]

        response = self.client.post('/api/airplanes/', data, format='json')

        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

        self.assertEqual(Airplane.objects.count(), 0)
