from django.test import TestCase
from ..models import Puppy

class PuppyTest(TestCase):
    # Test module for Puppy model

    def setup(self):
        Puppy.objects.create(
            name='Cooper', age=3, breed='Golden Retriever', color='Brown')
        Puppy.objects.create(
            name='Casper', age=1, breed='Gradane', color='Golden')

    def test_puppy_breed(self):
        puppy_casper = Puppy.objects.get(name='Casper')
        puppy_cooper = Puppy.objects.get(name='Cooper')
        self.assertEqual(
            puppy_casper.get_breed(), "Casper belongs to Gradane breed.")
        self.assertEqual(
            puppy_cooper.get_breed(), "Cooper belongs to Golden Retriever breed.")
