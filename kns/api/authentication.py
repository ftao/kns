from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import User, AnonymousUser
from django.contrib.auth import authenticate
from kns.api.models import APIToken
from piston.authentication import HttpBasicAuthentication

class APITokenAuthentication(object):
    """
    API Token authenticater. Synopsis:
    
    Authentication handlers must implement two methods:
     - `is_authenticated`: Will be called when checking for
        authentication. Receives a `request` object, please
        set your `User` object on `request.user`, otherwise
        return False (or something that evaluates to False.)
     - `challenge`: In cases where `is_authenticated` returns
        False, the result of this method will be returned.
        This will usually be a `HttpResponse` object with
        some kind of challenge headers and 401 code on it.
    """
    def __init__(self):
        pass

    def is_authenticated(self, request):
        username = request.GET.get('username', request.POST.get('username', None))
        token = request.GET.get('token', request.POST.get('token', None))
        try:
            api_token = APIToken.objects.get(token = token, user__username = username)
            request.user = api_token.user
        except APIToken.DoesNotExist:
            return False
        return not request.user in (False, None, AnonymousUser())
        
    def challenge(self):
        resp = HttpResponse("Authorization Required")
        resp['WWW-Authenticate'] = 'API Token' 
        resp.status_code = 401
        return resp

    def __repr__(self):
        return u'<APIToken Authoriaztion>' 


class MyHttpBasicAuthentication(HttpBasicAuthentication):

    def challenge(self):
        resp = HttpResponse("Authorization Required")
        resp['WWW-Authenticate'] = 'API Username Password' 
        resp.status_code = 401
        return resp
