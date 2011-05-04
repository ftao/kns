"""
Test for api app
"""

from django.test import TestCase,Client
from kns.api.models import APIToken
from django.contrib.auth.models import User
from django.http import HttpRequest
from kns.api.authentication import APITokenAuthentication
import simplejson as json
from django.core import mail

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
        request.GET['token'] = api_token
        request.GET['username'] = self.user.username
        self.assertTrue(auth.is_authenticated(request))

        request.GET = {}
        request.POST['token'] = api_token
        request.POST['username'] = self.user.username
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
        data['token'] = APIToken.get_user_token(self.user)
        data['username'] = 'test'
        response = client.post('/api/v1/knowledge/', data)
        self.assertEqual(response.status_code, 200)

        ret = json.loads(response.content)  
        expected = {
            u"tags": u"sf,answer,universe", 
            u"created_datetime": "2011-05-04 09:08:13", 
            u"question": u"what is answer of universe?", 
            u"id": 1, 
            u"user": {
                u"username": u"test"
            }, 
            u"answer_page_link": u"", 
            u"permlink": u"http://example.com/k/1.html", 
            u"search_keywords": u"", 
            u"answer_summary": u"42", 
            u"answer_page_title": u""
        }
        for key in ret.keys():
            if key not in [u'created_datetime']:
                self.assertEqual(ret[key], expected[key])

        data['include_answer_page'] = 'checked'
        data['search_keywords'] = 'universe answer\nthe answer of universe'
        response = client.post('/api/v1/knowledge/', data)
        self.assertEqual(response.status_code, 200)
        
        ret = json.loads(response.content)  
        expected = {
            u"tags": u"sf,answer,universe", 
            u"created_datetime": u"2011-05-04 09:15:09", 
            u"question": u"what is answer of universe?", 
            u"id": 2, 
            u"user": {
                u"username": u"test"
            }, 
            u"answer_page_link": u"http://42.com/42.html", 
            u"permlink": u"http://example.com/k/2.html", 
            u"search_keywords": u"universe answer\nthe answer of universe", 
            u"answer_summary": u"42", 
            u"answer_page_title": u"what is answer of universe?"
        }
        for key in ret.keys():
            if key not in [u'created_datetime']:
                self.assertEqual(ret[key], expected[key])


class UserAPITest(TestCase):

    def setUp(self):
        pass

    def testNewUser(self):
        client = Client()
        data = {
            'username' : 'test',
            'email' : 'test@test.com',
            'password' : 'pass',
        }
        response = client.post('/api/v1/user/', data)
        self.assertEqual(response.status_code, 200)
        self.assertEqual(json.loads(response.content)['username'], 'test')
        self.assertTrue(json.loads(response.content)['api_token'])
        #make sure we send an verify email
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Confirm email address for example.com')


class APITokenTest(TestCase):

    def setUp(self):
        self.user = User.objects.create(username = 'test')
        self.user.set_password('password')
        self.user.save()

        self.user2 = User.objects.create(username = 'test2')
        self.user2.set_password('password2')
        self.user2.save()

    def testNewUser(self):
        client = Client()

        import base64
        auth_value = base64.b64encode("%s:%s" %('test', 'password'))
        auth_header = {'HTTP_AUTHORIZATION':'Basic ' +  auth_value}

        response = client.get('/api/v1/apitoken/',  ** auth_header)
        self.assertEqual(response.status_code, 200)
        self.assertTrue('token' in json.loads(response.content))
        self.assertTrue('user' in json.loads(response.content))
        print response

    
