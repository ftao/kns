from django.conf.urls.defaults import *

urlpatterns = patterns('kns.release.views',
    url(r'^(?P<name>[\w\-]+)/update.xml$', 'update_manifest', name = "update_manifest"),
) 
