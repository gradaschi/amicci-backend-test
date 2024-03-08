from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from vendors.models import Vendor
import os


class VendorListTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = os.getenv('DJANGO_URL') + '/api/vendors/'

    def test_get_vendors_success(self):
        """Should return a list of vendors."""
        self.create_sample_vendors()

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(
            response.json()['description'], 'Fornecedores disponíveis')

        expected_data = [
            {'name': 'Fornecedor 1'},
            {'name': 'Fornecedor 2'}
        ]

        response_data = sorted(response.json()['data'], key=lambda x: x['id'])
        expected_data = sorted(expected_data, key=lambda x: x['name'])

        for i in response_data:
            i.pop('id')

        self.assertEqual(response_data, expected_data)

    def test_create_vendor_success(self):
        """Should create a new vendor."""
        data = {'name': 'Fornecedor exemplo'}

        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(response.json()['description'], f'Criado com sucesso. Id: {
                         response.json()["data"]["id"]}')
        self.assertEqual(response.json()['data']['name'], 'Fornecedor exemplo')

    def create_sample_vendors(self):
        Vendor.objects.create(name='Fornecedor 1')
        Vendor.objects.create(name='Fornecedor 2')


class VendorDetailTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.vendor = Vendor.objects.create(
            name='Fornecedor exemplo')
        self.url = os.getenv('DJANGO_URL') + \
            f'/api/vendors/{self.vendor.id}/'

    def test_get_vendor_success(self):
        """Should return a specific vendor."""

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(response.json()['description'], 'Fornecedor existe')
        self.assertEqual(response.json()['data']['name'], 'Fornecedor exemplo')

    def test_update_vendor_success(self):
        """Should update a specific vendor."""
        data = {'name': 'Fornecedor atualizado'}

        response = self.client.put(self.url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(
            response.json()['description'], f'Atualizado com sucesso. Id: {self.vendor.id}')
        self.assertEqual(Vendor.objects.get(
            id=self.vendor.id).name, 'Fornecedor atualizado')

    def test_delete_vendor_success(self):
        """Should delete a specific vendor."""
        response = self.client.delete(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        with self.assertRaises(Vendor.DoesNotExist):
            Vendor.objects.get(id=self.vendor.id)
