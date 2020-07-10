from unittest.mock import patch
from django.test import TestCase
from django.contrib.auth import get_user_model
from core import models

def sample_user(email='test@rahali.com', password='pass123'):
    """ Create a sample user """
    return get_user_model().objects.create_user(email, password)


class ModelTest(TestCase):

    def test_create_user_with_email_successfully(self):
        """ Test creating user with email """
        email = 'test@gmail.com'
        password = 'pass123'

        user = get_user_model().objects.create_user(
            email=email,
            password=password
        )

        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_new_user_email_normalized(self):
        email = 'test@GMAIL.COM'
        user = get_user_model().objects.create_user(
            email=email,
            password='balabla'
        )

        self.assertEqual(user.email, email.lower())

    def test_new_user_invalid_email(self):
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(
                email=None,
                password='balabla'
            )

    def test_create_superuser(self):
        """ Test creating user with email """
        email = 'test@gmail.com'
        password = 'pass123'

        user = get_user_model().objects.create_superuser(
            email=email,
            password=password
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)

    def test_tag_str(self):
        """ Test the tag string representation"""
        tag = models.Tag.objects.create(
            user=sample_user(),
            name='vegan'
        )

        self.assertEqual(str(tag), tag.name)

    def test_ingredient_str(self):
        """ Test Ingredient representation """
        ingredient = models.Ingredient.objects.create(
            user=sample_user(),
            name='Cucumber'
        )

        self.assertEqual(str(ingredient), ingredient.name)

    def test_recipe_str(self):
        """ Test Recipe representation """
        recipe = models.Recipe.objects.create(
            user=sample_user(),
            title='Steak and mushrooms sauce',
            time_minutes=5,
            price=5.00,
        )

        self.assertEqual(str(recipe), recipe.title)

    @patch('uuid.uuid4')
    def test_recipe_filename_uuid(self, mock_uuid):
        """ Test that image is saved in the correct location """
        uuid = 'test-uuid'
        mock_uuid.return_value = uuid
        file_path = models.recipe_image_file_path(None, 'image.jpg')

        exp_path = f'uploads/recipe/{uuid}.jpg'
        self.assertEqual(file_path, exp_path)

