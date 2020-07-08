from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status

CREATE_USER_URL = reverse('user:create')
TOKEN_URL = reverse('user:token')
MYACCOUNT_URL = reverse('user:me')


def create_user(**param):
    return get_user_model().objects.create_user(**param)


class PublicUserAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_create_valid_user_success(self):
        """ Test Creating a user with a valid payload """
        payload = {
            'name': 'mdrahali',
            'email': 'test@rahali.com',
            'password': 'pass123',
        }

        res = self.client.post(CREATE_USER_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        user = get_user_model().objects.get(**res.data)
        self.assertTrue(user.check_password(payload['password']))
        self.assertNotIn('password', res.data)

    def test_create_user_exist(self):
        """ Test Creating a user that already exist """

        payload = {
            'name': 'mdrahali',
            'email': 'test@rahali.com',
            'password': 'pass123',
        }

        create_user(**payload)
        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_too_short(self):
        """ password should more than 5 caracters """
        payload = {
            'name': 'mdrahali',
            'email': 'test@rahali.com',
            'password': 'pwd',
        }

        res = self.client.post(CREATE_USER_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)
        user_exist = get_user_model().objects.filter(email=payload['email']).exists()
        self.assertFalse(user_exist)

    def test_create_token_for_user(self):
        """ Test that a token is created for the user  """
        payload = {
            'name': 'mdrahali',
            'email': 'test@rahali.com',
            'password': 'pass123',
        }

        create_user(**payload)
        res = self.client.post(TOKEN_URL, payload)
        self.assertIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    def test_create_user_invalid_credentials(self):
        create_user(email='test@rahali.com', password='pass123')
        payload = {
            'name': 'mdrahali',
            'email': 'test@rahali.com',
            'password': 'wrong',
        }
        res = self.client.post(TOKEN_URL, payload)

        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_create_token_no_user(self):
        payload = {
            'name': 'mdrahali',
            'email': 'test@rahali.com',
            'password': 'wrong',
        }

        res = self.client.post(TOKEN_URL, payload)

        self.assertNotIn('token', res.data)
        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

    def test_retrieve_user_unauthorized(self):
        """ Test that authentication is required to retrieve user info """

        res = self.client.get(MYACCOUNT_URL)
        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateUserAPITest(TestCase):
    """ Test that need User Authentication  """

    def setUp(self):
        payload = {
            'name': 'mdrahali',
            'email': 'test@rahali.com',
            'password': 'pass123',
        }
        self.user = create_user(**payload)
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_retrieve_profile_success(self):
        res = self.client.get(MYACCOUNT_URL)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, {'name': 'mdrahali', 'email': 'test@rahali.com'})

    def test_post_not_allowed(self):
        """ Test that POST method is not allowed on the /me url """

        res = self.client.post(MYACCOUNT_URL)
        self.assertEqual(res.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_update_user_profile(self):
        payload = {
            'name': 'new name',
            'email': 'new_email@rahali.com',
            'password': 'newpass',
        }
        res = self.client.patch(MYACCOUNT_URL, payload)

        self.user.refresh_from_db()
        self.assertEqual(self.user.name, payload['name'])
        self.assertTrue(self.user.check_password(payload['password']))
        self.assertEqual(res.status_code, status.HTTP_200_OK)

    
