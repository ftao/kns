from django.conf.urls.defaults import *
from django.views.generic import list_detail 
from kns.knowledge.models import Knowledge

knowledge_info =  {
    #'template_name': 'index.html',
    'queryset': Knowledge.objects.all(), # only here, what could be wrong?
    'template_object_name' : 'knowledge',
}

urlpatterns = patterns('',
    url(r'^k/(?P<object_id>\d+).html$', list_detail.object_detail, knowledge_info, name="knowledge_detail"),
) 
