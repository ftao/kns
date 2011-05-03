"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase,Client
from django.contrib.auth.models import User
from kns.knowledge.models import Knowledge

class KnowledgeTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username = 'test', password = 'pass')
        self.knowledge = Knowledge.objects.create(question = 'question', answer_summary = 'answer', user = self.user)

    def test_knowledge(self):
        """
        """
        client = Client()
        response = client.get('/k/%d.html' %self.knowledge.id)
        self.assertEqual(response.status_code, 200)
        print response

 
class HomeTest(TestCase):

    def test_home(self):
        """
        """
        client = Client()
        response = client.get('/')
        print response
        self.assertEqual(response.status_code, 200)
        print response


