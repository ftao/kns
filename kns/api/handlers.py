import datetime
from piston.handler import BaseHandler
from piston.utils import rc
from kns.knowledge.models import Knowledge
from django.conf import settings

class KnowledgeHandler(BaseHandler):
    allowed_methods = ('POST',)
    model = Knowledge
    fields = ('id', 'question',
              'answer_summary','answer_page_title', 'answer_page_link',
              'tags', 'created_datetime',
              ('user', ('username',)))

    def create(self, request):
        """
        Creates a new knowledge entry.
        """
        if not hasattr(request, "data"):
            request.data = request.POST
        attrs = self.flatten_dict(request.data)
        if 'api_token' in attrs:
            del attrs['api_token']
        if self.exists(**attrs):
            return rc.DUPLICATE_ENTRY
        else:
            kn = Knowledge(question = attrs['question'], 
                            answer_summary = attrs['answer_summary'],
                            answer_page_title = attrs['answer_page_title'],
                            answer_page_link = attrs['answer_page_link'],
                            tags = attrs['tags'],
                            user=request.user)
            kn.save()
            return kn
