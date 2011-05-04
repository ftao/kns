from django.conf.urls.defaults import *
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from piston.doc import documentation_view
from kns.api.authentication import APITokenAuthentication
from kns.api.handlers import KnowledgeHandler,UserHandler,APITokenHandler

api_token_auth = APITokenAuthentication()
knowledge_resource = Resource(handler=KnowledgeHandler, authentication=api_token_auth)
user_resource = Resource(handler=UserHandler)

auth = HttpBasicAuthentication(realm="API")
apitoken_resource = Resource(handler=APITokenHandler, authentication = auth)

urlpatterns = patterns('',
    url(r'^user/$', user_resource, name="user"),
    url(r'^knowledge/$', knowledge_resource, name="knowledge"),
    url(r'^apitoken/$', apitoken_resource, name="apitoken"),
) 
