import os
import tempfile
from PIL import Image

from django.contrib.auth import get_user_model
from django.urls import reverse
from django.test import TestCase

from rest_framework import status
from rest_framework.test import APIClient
from core.models import Recipe, Tag, Ingredient
from recipe.serializers import RecipeSerializer, RecipeDetailSerializer

RECIPES_URL = reverse('recipe:recipe-list')


def detail_urls(recipe_id):
    # /api/recipe/recipes/1/
    return reverse('recipe:recipe-detail', args=[recipe_id])


def image_upload_url(recipe_id):
    """Return URL for recipe image upload"""
    return reverse('recipe:recipe-upload-image', args=[recipe_id])


def sample_tags(user, name='Main Course'):
    return Tag.objects.create(user=user, name=name)


def sample_ingredients(user, name='Kale'):
    return Ingredient.objects.create(user=user, name=name)


def sample_recipe(user, **params):
    defaults = {
        'title': 'Sample recipes',
        'time_minutes': 10,
        'price': 5.00
    }

    defaults.update(params)
    return Recipe.objects.create(user=user, **defaults)


class PublicRecipeAPITest(TestCase):

    def setUp(self):
        self.client = APIClient()

    def test_auth_required(self):
        res = self.client.get(RECIPES_URL)

        self.assertEqual(res.status_code, status.HTTP_401_UNAUTHORIZED)


class PrivateRecipeAPITest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            'test@rahali.com',
            'pass123'
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)

    def test_retrieve_recipes(self):
        sample_recipe(user=self.user)
        res = self.client.get(RECIPES_URL)

        recipes = Recipe.objects.all().order_by('-id')
        serializer = RecipeSerializer(recipes, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_retrieve_recipes_limited_to_user(self):
        user_2 = get_user_model().objects.create_user(
            'user_2@rahali.com',
            'pass123'
        )

        sample_recipe(user=self.user)
        sample_recipe(user=user_2)
        res = self.client.get(RECIPES_URL)
        recipes = Recipe.objects.filter(user=self.user)
        serializer = RecipeSerializer(recipes, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)
        self.assertEqual(len(res.data), 1)
        self.assertEqual(res.data[0]['title'], 'Sample recipes')

    def test_view_recipe_detail(self):
        recipe = sample_recipe(user=self.user)
        recipe.tags.add(sample_tags(user=self.user))
        recipe.ingredients.add(sample_ingredients(user=self.user))

        url = detail_urls(recipe.id)

        res = self.client.get(url)
        serializer = RecipeDetailSerializer(recipe)

        self.assertEqual(res.data, serializer.data)

    def test_create_basic_recipe(self):
        """ Test creating a basic recipe """
        payload = {
            'title': 'Chocolate cheesecake',
            'time_minutes': 20,
            'price': 6.00
        }

        res = self.client.post(RECIPES_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        recipe = Recipe.objects.get(id=res.data['id'])
        for key in payload.keys():
            self.assertEqual(payload[key], getattr(recipe, key))

    def test_create_recipe_with_tags(self):
        tag_1 = sample_tags(user=self.user, name='Vegan')
        tag_2 = sample_tags(user=self.user, name='Dessert')

        payload = {
            'title': 'Avocado lime',
            'tags': [tag_1.id, tag_2.id],
            'time_minutes': 20,
            'price': 6.00,
        }
        res = self.client.post(RECIPES_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        recipe = Recipe.objects.get(id=res.data['id'])
        tags = recipe.tags.all()
        self.assertEqual(tags.count(), 2)
        self.assertIn(tag_1, tags)
        self.assertIn(tag_2, tags)

    def test_create_recipe_with_ingredient(self):
        ingredient_1 = sample_ingredients(user=self.user, name='Kale')
        ingredient_2 = sample_ingredients(user=self.user, name='Salt')

        payload = {
            'title': 'Chocolat',
            'time_minutes': 20,
            'ingredients': [ingredient_1.id, ingredient_2.id],
            'price': 6.00,
        }

        res = self.client.post(RECIPES_URL, payload)
        self.assertEqual(res.status_code, status.HTTP_201_CREATED)
        recipe = Recipe.objects.get(id=res.data['id'])
        ingredients = recipe.ingredients.all()
        self.assertEqual(ingredients.count(), 2)
        self.assertIn(ingredient_1, ingredients)
        self.assertIn(ingredient_2, ingredients)

    def test_partial_recipe_update(self):
        recipe = sample_recipe(user=self.user)
        recipe.tags.add(sample_tags(user=self.user))
        new_tag = sample_tags(user=self.user, name='Curry')

        payload = {'title': 'Chicken tikka', 'tags': [new_tag.id]}
        url = detail_urls(recipe.id)
        self.client.patch(url, payload)

        recipe.refresh_from_db()
        self.assertEqual(recipe.title, payload['title'])
        tags = recipe.tags.all()
        self.assertEqual(len(tags), 1)
        self.assertIn(new_tag, tags)

    def test_full_recipe_update(self):
        recipe = sample_recipe(user=self.user)
        recipe.tags.add(sample_tags(user=self.user))
        payload = {
            'title': 'spaghetti carbonara',
            'time_minutes': 25,
            'price': 5.00,
        }

        url = detail_urls(recipe.id)
        self.client.put(url, payload)

        recipe.refresh_from_db()
        self.assertEqual(recipe.title, payload['title'])
        self.assertEqual(recipe.time_minutes, payload['time_minutes'])
        self.assertEqual(recipe.price, payload['price'])
        tags = recipe.tags.all()
        self.assertEqual(len(tags), 0)


class RecipeImageUploadTests(TestCase):
    def setUp(self):
        self.user = get_user_model().objects.create_user(
            'test@rahali.com',
            'pass123'
        )
        self.client = APIClient()
        self.client.force_authenticate(user=self.user)
        self.recipe = sample_recipe(user=self.user)

    def tearDown(self):
        self.recipe.image.delete()

    def test_upload_image_to_recipe(self):
        """Test uploading an image to recipe"""
        url = image_upload_url(self.recipe.id)
        with tempfile.NamedTemporaryFile(suffix='.jpg') as ntf:
            img = Image.new('RGB', (10, 10))
            img.save(ntf, format='JPEG')
            ntf.seek(0)
            res = self.client.post(url, {'image': ntf}, format='multipart')

        self.recipe.refresh_from_db()
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIn('image', res.data)
        self.assertTrue(os.path.exists(self.recipe.image.path))

    def test_upload_image_bad_request(self):
        url = image_upload_url(self.recipe.id)
        res = self.client.post(url, {'image': 'not_image'}, format='multipart')

        self.assertEqual(res.status_code, status.HTTP_400_BAD_REQUEST)

