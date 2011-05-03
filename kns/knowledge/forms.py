from django.forms import ModelForm
from kns.knowledge.models import Knowledge

class KnowledgeForm(ModelForm):
    class Meta:
        model = Knowledge
        exclude = ('user',)
