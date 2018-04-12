"""
This file demonstrates writing tests using the unittest module. These will pass
when you run "manage.py test".

Replace this with more appropriate tests for your application.
"""

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.core.urlresolvers import reverse


class SimpleTest(TestCase):
    def test_basic_addition(self):
        """
        Tests that 1 + 1 always equals 2.
        """
        self.assertEqual(1 + 1, 2)

    def test_api_run_assimilite(self):
        """Test the api has bucket creation capability."""
        results=["testing"]
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, results)


