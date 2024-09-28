# inventory/tests.py
from rest_framework.test import APITestCase
from rest_framework import status
from .models import Item

class ItemTests(APITestCase):
    
    def test_create_item(self):
        response = self.client.post('/api/items/', {'name': 'Item1', 'description': 'Description'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)

    def test_retrieve_item(self):
        item = Item.objects.create(name='Item1', description='Description')
        response = self.client.get(f'/api/items/{item.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    # Add more tests for update, delete, and error cases...
