
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from user_control.models import User


class RegistrationViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()

    def test_registration_success(self):
        new_user_data = {
            "username": "mir",
            "email": "test@example.com",
            "password": "password123",
            "business_name": "Test Business",
            "mailing_address": "123 Test St",
            "contact_name": "John Doe",
            "contact_title": "Manager",
            "phone_number": "1234567890"
        }
        response = self.client.post('/users/signup/', new_user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertIn('token', response.data)

    def test_registration_invalid_data(self):
        invalid_data = {
            'email': 'invalidemail',
            'password': 'password'
        }
        response = self.client.post('/users/signup/', invalid_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
