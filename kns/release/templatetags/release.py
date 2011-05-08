from django import template
register = template.Library()
from kns.release.models import Release

@register.filter
def release_url(name):
    try:
        release = Release.objects.filter(name = name).order_by('-released_time', '-id')[0]
        return release.url
    except IndexError,e:
        return ''
