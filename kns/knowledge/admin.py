from django.contrib import admin
from kns.knowledge.models import Knowledge

class KnowledgeAdmin(admin.ModelAdmin):
    list_display = ('user', 'question', 'tags')

admin.site.register(Knowledge, KnowledgeAdmin)

