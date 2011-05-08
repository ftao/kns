#coding=utf-8
"""
This file demonstrates two different styles of tests (one doctest and one
unittest). These will both pass when you run "manage.py test".

Replace these with more appropriate tests for your application.
"""

from django.test import TestCase,Client
from django.contrib.auth.models import User
import urllib
from kns.knowledge.models import Knowledge

class UserTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username = 'test', password = 'pass')

    def test_user(self):
        """
        """
        client = Client()
        response = client.get('/users/%s/' %urllib.quote(self.user.username))
        self.assertEqual(response.status_code, 200)
#        print response


    def test_user_feed(self):
        Knowledge.objects.create(question = u'问题how to ', search_keywords = u'how to',
                answer_page_link = u'http://g.cn', answer_page_title = 'google',
                tags = u'a,问题', answer_summary = u'summary', user = self.user)
        Knowledge.objects.create(question = u'a', tags = u'a,问题', user = self.user)

        client = Client()
        response = client.get('/users/%s/feed/' %urllib.quote(self.user.username))
        self.assertEqual(response.status_code, 200)
#        print response
        
