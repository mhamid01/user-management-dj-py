from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from user_control.models import User


class LoginViewTests(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.user_data = {
            'email': 'test@example.com',
            'password': 'testpassword'
        }
        self.user = User.objects.create_user(email=self.user_data['email'], password=self.user_data['password'])

    def test_login_success(self):
        response = self.client.post('/users/signin/', self.user_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn('token', response.data)

    def test_login_invalid_password(self):
        invalid_password_data = {
            'email': 'test@example.com',
            'password': 'wrongpassword'
        }
        response = self.client.post('/users/signin/', invalid_password_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_login_user_not_found(self):
        invalid_email_data = {
            'email': 'nonexistent@example.com',
            'password': 'testpassword'
        }
        response = self.client.post('/users/signin/', invalid_email_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
