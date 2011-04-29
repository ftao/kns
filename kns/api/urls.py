from django.conf.urls.defaults import *
from piston.resource import Resource
from piston.authentication import HttpBasicAuthentication
from piston.doc import documentation_view
from kns.api.authentication import APITokenAuthentication
from kns.api.handlers import KnowledgeHandler

api_token_auth = APITokenAuthentication()
knowledge_resource = Resource(handler=KnowledgeHandler, authentication=api_token_auth)

urlpatterns = patterns('',
    url(r'^knowledge/$', knowledge_resource, name="knowledge"),
) 