from django.conf.urls.defaults import *
from django.views.generic import list_detail 
from django.contrib.auth.models import User
from kns.profile.feeds import UserKnowledgeFeed

user_info =  {
    'queryset': User.objects.all(),
    'template_object_name' : 'theuser',
}

user_info_via_username =  {
    'queryset': User.objects.all(),
    'template_object_name' : 'theuser',
    'slug_field' : 'username',
}

urlpatterns = patterns('',
#    url(r'^user/(?P<object_id>\d+).html$', list_detail.object_detail, user_info, name="user_detail"),
    url(r'^users/(?P<slug>\w+)/$', list_detail.object_detail, user_info_via_username, name="user_detail"),
    url(r'^users/(?P<username>\w+)/feed/$', UserKnowledgeFeed(), name="user_knowledge_feed"),
) 
