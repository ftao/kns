"""
Test for api app
"""

from django.test import TestCase,Client
from kns.api.models import APIToken
from django.contrib.auth.models import User
from django.http import HttpRequest
from kns.api.authentication import APITokenAuthentication
import simplejson as json

class APITokenAuthenticationTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username = 'test', password = 'pass')

    def test_api_token(self):
        auth = APITokenAuthentication()
        request = HttpRequest()
        request.META = {}
        request.GET = {}
        self.assertTrue(not auth.is_authenticated(request))
        request.POST = {}
        self.assertTrue(not auth.is_authenticated(request))

        api_token = APIToken.get_user_token(self.user)
        request.GET['api_token'] = api_token
        self.assertTrue(auth.is_authenticated(request))

        request.GET = {}
        request.POST['api_token'] = api_token
        self.assertTrue(auth.is_authenticated(request))

        request.GET = {}
        request.POST = {}
        request.META['X-API-TOKEN'] = api_token
        self.assertTrue(auth.is_authenticated(request))

    def test_challenge(self):
        auth = APITokenAuthentication()
        resp = auth.challenge()
        self.assertEqual(resp.status_code , 401)

class KnowledgeAPITest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username = 'test', password = 'pass')

    def testNewKnowledge(self):
        client = Client()
        data = {
            'question' : 'what is answer of universe?',
            'answer_summary' : '42',
            'answer_page_link': 'http://42.com/42.html',
            'answer_page_title': 'what is answer of universe?',
            'tags' : 'sf,answer,universe',
        }
        response = client.post('/api/v1/knowledge/', data)
        self.assertEqual(response.status_code, 401)
        data['api_token'] = APIToken.get_user_token(self.user)
        response = client.post('/api/v1/knowledge/', data)
        print response
        self.assertEqual(response.status_code, 200)


class UserAPITest(TestCase):

    def setUp(self):
        pass

    def testNewKnowledge(self):
        client = Client()
        data = {
            'username' : 'test',
            'email' : 'test@test.com',
        }
        response = client.post('/api/v1/user/', data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['username'], 'test')
        self.assertTrue(json.loads(response.content)['api_token'])
        print response


