from django.template import RequestContext
from django.shortcuts import render_to_response
from kns.release.models import Release

def update_manifest(request, name):
    release = Release.objects.filter(name = name).order_by('-released_time').get()
    return render_to_response('release/update.xml',
        {'release' : release },
        context_instance = RequestContext(request),
        mimetype = 'application/xml',
    )

