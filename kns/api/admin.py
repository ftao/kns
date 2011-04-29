from django.contrib import admin
from kns.api.models import APIToken

class APITokenAdmin(admin.ModelAdmin):
    list_display = ('user', 'token')

admin.site.register(APIToken, APITokenAdmin)

