from django.contrib import admin
from kns.release.models import Release

class ReleaseAdmin(admin.ModelAdmin):
    list_display = ('name', 'appid', 'version', 'url', 'released_time')

admin.site.register(Release, ReleaseAdmin)

