from django.conf.urls.defaults import *
from django.conf import settings
from django.views.generic.simple import direct_to_template

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Example:
    (r'^$', direct_to_template, {'template': 'index.html'}),
    (r'^api/v1/', include('kns.api.urls')),
    (r'^release/', include('kns.release.urls')),
    (r'^', include('kns.knowledge.urls')),
    (r'^', include('kns.profile.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    (r'^confirm_email/(\w+)/$', 'emailconfirmation.views.confirm_email'),
    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),
    (r'^static/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),
)

urlpatterns += patterns('',
    (r'^sentry314/', include('sentry.urls')),
)

