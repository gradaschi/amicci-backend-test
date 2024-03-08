from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from briefings.models import Briefing
import os


class BriefingListTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = os.getenv('DJANGO_URL') + '/api/briefings/'

    def test_get_briefings_success(self):
        """Should return a list of briefings."""
        self.create_sample_briefings()

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(
            response.json()['description'], 'Briefings disponíveis')

        expected_data = [
            {'name': 'Briefing 1', 'retailer': 'Retailer 1', 'responsible': 'Responsible 1',
             'category': 'Category 1', 'release_date': '2022-01-01', 'available': 10},
            {'name': 'Briefing 2', 'retailer': 'Retailer 2', 'responsible': 'Responsible 2',
             'category': 'Category 2', 'release_date': '2022-01-02', 'available': 15}
        ]

        response_data = sorted(response.json()['data'], key=lambda x: x['id'])
        expected_data = sorted(expected_data, key=lambda x: x['name'])

        for i in response_data:
            i.pop('id')

        self.assertEqual(response_data, expected_data)

    def test_create_briefing_success(self):
        """Should create a new briefing."""
        data = {'name': 'Briefing exemplo', 'retailer': 'Retailer exemplo', 'responsible': 'Responsável exemplo',
                'category': 'Categoria exemplo', 'release_date': '2022-01-03', 'available': 5}

        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(response.json()['description'], f'Criado com sucesso. Id: {
                         response.json()["data"]["id"]}')
        self.assertEqual(response.json()['data']['name'], 'Briefing exemplo')

    def create_sample_briefings(self):
        Briefing.objects.create(name='Briefing 1', retailer='Retailer 1', responsible='Responsible 1',
                                category='Category 1', release_date='2022-01-01', available=10)
        Briefing.objects.create(name='Briefing 2', retailer='Retailer 2', responsible='Responsible 2',
                                category='Category 2', release_date='2022-01-02', available=15)


class BriefingDetailTestCase(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.briefing = Briefing.objects.create(name='Briefing exemplo', retailer='Retailer exemplo',
                                                responsible='Responsável exemplo', category='Categoria exemplo', release_date='2022-01-03', available=5)
        self.url = os.getenv('DJANGO_URL') + \
            f'/api/briefings/{self.briefing.id}/'

    def test_get_briefing_success(self):
        """Should return a specific briefing."""

        response = self.client.get(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(response.json()['description'], 'Briefing existe')
        self.assertEqual(response.json()['data']['name'], 'Briefing exemplo')

    def test_update_briefing_success(self):
        """Should update a specific briefing."""
        data = {'name': 'Briefing atualizado', 'retailer': 'Retailer atualizado', 'responsible': 'Responsável atualizado',
                'category': 'Categoria atualizado', 'release_date': '2022-01-03', 'available': 5}

        response = self.client.put(self.url, data)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response['Content-Type'], 'application/json')
        self.assertEqual(
            response.json()['description'], f'Atualizado com sucesso. Id: {self.briefing.id}')
        self.assertEqual(Briefing.objects.get(
            id=self.briefing.id).name, 'Briefing atualizado')

    def test_delete_briefing_success(self):
        """Should delete a specific briefing."""
        response = self.client.delete(self.url)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        with self.assertRaises(Briefing.DoesNotExist):
            Briefing.objects.get(id=self.briefing.id)
