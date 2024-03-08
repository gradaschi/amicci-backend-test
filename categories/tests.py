from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from categories.models import Category
import os


class CategoryListTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = os.getenv('DJANGO_URL') + '/api/categories/'

    def test_get_categories_success(self):
        """Should return a list of categories."""
        self.create_sample_categories()

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(
            response.json()['description'], 'Categorias disponíveis')

        expected_data = [
            {'name': 'Categoria 1', 'description': 'Descrição 1'},
            {'name': 'Categoria 2', 'description': 'Descrição 2'}
        ]

        response_data = sorted(response.json()['data'], key=lambda x: x['id'])
        expected_data = sorted(expected_data, key=lambda x: x['name'])

        for i in response_data:
            i.pop('id')

        self.assertEqual(response_data, expected_data)

    def test_create_category_success(self):
        """Should create a new category."""
        data = {'name': 'Categoria exemplo',
                'description': 'Descrição exemplo'}

        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(response.json()['description'], f'Criado com sucesso. Id: {
                         response.json()["data"]["id"]}')
        self.assertEqual(response.json()['data']['name'], 'Categoria exemplo')

    def create_sample_categories(self):
        Category.objects.create(name='Categoria 1', description='Descrição 1')
        Category.objects.create(name='Categoria 2', description='Descrição 2')


class CategoryDetailTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.category = Category.objects.create(
            name='Categoria exemplo', description='Descrição exemplo')
        self.url = os.getenv('DJANGO_URL') + \
            f'/api/categories/{self.category.id}/'

    def test_get_category_success(self):
        """Should return a specific category."""

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(response.json()['description'], 'Categoria existe')
        self.assertEqual(response.json()['data']['name'], 'Categoria exemplo')

    def test_update_category_success(self):
        """Should update a specific category."""
        data = {'name': 'Categoria atualizada',
                'description': 'Descrição atualizada'}

        response = self.client.put(self.url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(
            response.json()['description'], f'Atualizado com sucesso. Id: {self.category.id}')
        self.assertEqual(Category.objects.get(
            id=self.category.id).name, 'Categoria atualizada')

    def test_delete_category_success(self):
        """Should delete a specific category."""
        response = self.client.delete(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        with self.assertRaises(Category.DoesNotExist):
            Category.objects.get(id=self.category.id)
