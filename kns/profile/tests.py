"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase,Client
from django.contrib.auth.models import User
import urllib

class UserTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username = 'test', password = 'pass')

    def test_user(self):
        """
        """
        client = Client()

        response = client.get('/user/%s.html' %urllib.quote(self.user.username))
        self.assertEqual(response.status_code, 200)
        print response


