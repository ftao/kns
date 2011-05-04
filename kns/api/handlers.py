import datetime
from piston.handler import BaseHandler
from piston.utils import rc,validate
from kns.knowledge.models import Knowledge
from kns.knowledge.forms import KnowledgeForm
from django.conf import settings
from django.contrib.auth.models import User
from django.contrib.sites.models import Site
from kns.api.models import APIToken
from emailconfirmation.models import EmailAddress
from kns.api.forms import SignupForm

class UserHandler(BaseHandler):
    allowed_methods = ('POST',)
    model = User
    fields = ('username', 'api_token')

    anonymous = True

    @validate(SignupForm, 'POST')
    def create(self, request):
        """
        Creates a new knowledge entry.
        """
        if not hasattr(request, "data"):
            request.data = request.POST
        attrs = self.flatten_dict(request.data)

        username = attrs['username']
        email = attrs['email']
        password = attrs['password']
        same_name_count = User.objects.filter(username = username).count()
        if same_name_count:
            return RC.DUPLICATE_ENTRY
        user = User(username = username, email = email)
        user.set_password(password)
        user.save()
        user.message_set.create(message="Confirmation email sent to %s" % email)
        EmailAddress.objects.add_email(user, email)
        return user

    @classmethod
    def api_token(cls, user):
        return APIToken.objects.get(user = user).token

class APITokenHandler(BaseHandler):
    allowed_methods = ('GET',)
    model = APIToken
    fields = ('token', ('user', ('username',)))

    def read(self, request):
        return APIToken.objects.get(user = request.user)


class KnowledgeHandler(BaseHandler):
    allowed_methods = ('POST',)
    model = Knowledge
    fields = ('id', 'question',
              'search_keywords',
              'answer_summary','answer_page_title', 'answer_page_link',
              'tags', 'created_datetime',
              'permlink',
              ('user', ('username',)))

    @validate(KnowledgeForm, 'POST')
    def create(self, request):
        """
        Creates a new knowledge entry.
        """
        if not hasattr(request, "data"):
            request.data = request.POST
        attrs = self.flatten_dict(request.data)
        if not attrs.get('include_answer_page', None):
            if 'answer_page_title' in attrs:
                del attrs['answer_page_title']
            if 'answer_page_link' in attrs:
                del attrs['answer_page_link']
        kn = Knowledge(question = attrs['question'], 
                        search_keywords = attrs.get('search_keywords', ''),
                        answer_summary = attrs.get('answer_summary', ''),
                        answer_page_title = attrs.get('answer_page_title', ''),
                        answer_page_link = attrs.get('answer_page_link', ''),
                        tags = attrs.get('tags', ''),
                        user=request.user)
        kn.save()
        return kn

    @classmethod
    def permlink(cls, knowledge):
        return  u'http://%s%s' %(Site.objects.get_current().domain, knowledge.get_absolute_url())
