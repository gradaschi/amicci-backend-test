from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from retailers.models import Retailer
from vendors.models import Vendor
import os


class RetailerListTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = os.getenv('DJANGO_URL') + '/api/retailers/'
        """Should return a list of retailers."""
        self.create_sample_retailers()

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(
            response.json()['description'], 'Varejistas disponíveis')

        expected_data = [
            {'name': 'Varejista 1', 'vendors': []},
            {'name': 'Varejista 2', 'vendors': []}
        ]

        response_data = sorted(response.json()['data'], key=lambda x: x['id'])
        expected_data = sorted(expected_data, key=lambda x: x['name'])

        for i in response_data:
            i.pop('id')

        self.assertEqual(response_data, expected_data)


class RetailerDetailTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.vendor = Vendor.objects.create(name='Fornecedor exemplo')
        self.retailer = Retailer.objects.create(
            name='Varejista exemplo')
        self.retailer.vendors.add(self.vendor)
        self.url = os.getenv('DJANGO_URL') + \
            f'/api/retailers/{self.retailer.id}/'

    def test_update_retailer_success(self):
        """Should update a specific retailer."""
        data = {'name': 'Varejista atualizado', 'vendors': [self.vendor.id]}

        response = self.client.put(self.url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(
            response.json()['description'], f'Atualizado com sucesso. Id: {self.retailer.id}')
        self.assertEqual(Retailer.objects.get(
            id=self.retailer.id).name, 'Varejista atualizado')

    def test_delete_retailer_success(self):
        """Should delete a specific retailer."""
        response = self.client.delete(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        with self.assertRaises(Retailer.DoesNotExist):
            Retailer.objects.get(id=self.retailer.id)
