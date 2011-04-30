import datetime
from piston.handler import BaseHandler
from piston.utils import rc
from kns.knowledge.models import Knowledge
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from kns.api.models import APIToken

class UserHandler(BaseHandler):
    allowed_methods = ('POST',)
    model = User
    fields = ('username', 'api_token')

    anonymous = True

    def create(self, request):
        """
        Creates a new knowledge entry.
        """
        if not hasattr(request, "data"):
            request.data = request.POST
        attrs = self.flatten_dict(request.data)

        username = attrs['username']
        email = attrs['email']
        same_name_count = User.objects.filter(username = username).count()
        if same_name_count:
            return RC.DUPLICATE_ENTRY
        same_email_count = User.objects.filter(email = email).count()
        if same_email_count:
            return RC.DUPLICATE_ENTRY
        user = User(username = username, email = email)
        user.save()
        return user

    @classmethod
    def api_token(cls, user):
        return APIToken.objects.get(user = user).token

class KnowledgeHandler(BaseHandler):
    allowed_methods = ('POST',)
    model = Knowledge
    fields = ('id', 'question',
              'answer_summary','answer_page_title', 'answer_page_link',
              'tags', 'created_datetime',
              'permlink',
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

    @classmethod
    def permlink(cls, knowledge):
        return  u'http://%s%s' %(Site.objects.get_current().domain, knowledge.get_absolute_url())
