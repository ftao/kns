from django.conf.urls.defaults import *
from django.views.generic import list_detail 
from django.contrib.auth.models import User

user_info =  {
    'queryset': User.objects.all(),
    'template_object_name' : 'theuser',
}

urlpatterns = patterns('',
    url(r'^user/(?P<object_id>\d+).html$', list_detail.object_detail, user_info, name="user_detail"),
) 
