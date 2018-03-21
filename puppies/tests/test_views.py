import json
from rest_framework import status
from django.test import TestCase, Client
from django.urls import reverse
from ..models import Puppy
from ..serializers import PuppySerializer

client = Client()

class GetAllPuppiesTest(TestCase):

    def setUp(self):
        Puppy.objects.create(
            name='Casper', age=3, breed='Bull Dog', color='Black')

        Puppy.objects.create(
            name='Muffin', age=1, breed='Gradane', color='Brown')

        Puppy.objects.create(
            name='Rambo', age=2, breed='Labrador', color='Black')

        Puppy.objects.create(
            name='Ricky', age=6, breed='Labrador', color='Brown')

    def test_get_all_puppies(self):
        # Add objects to API and DB, get response from API.
        response = client.get(reverse('get_post_puppies'))
        # Get objects from DB.
        puppies = Puppy.objects.all()
        # Check if there's many objects returned.
        serializer = PuppySerializer(puppies, many=True)
        # Check if DB query equals API query.
        self.assertEqual(response.data, serializer.data)
        # Check if response status is 200.
        self.assertEqual(response.status_code, status.HTTP_200_OK)
