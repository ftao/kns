from django.contrib.syndication.views import Feed
from django.contrib.sites.models import Site
from django.contrib.auth.models import User
from django.shortcuts import get_object_or_404
from kns.knowledge.models import Knowledge

class UserKnowledgeFeed(Feed):

    description_template = 'feeds/knowledge_description.html'

    def get_object(self, request, username):
        return get_object_or_404(User, username=username)

    def title(self, obj):
        current_site = Site.objects.get_current()
        return u"%s: %s's knowledge" % (current_site.name, obj.username)

    def link(self, obj):
        return obj.get_absolute_url() + 'feed/'

    def description(self, obj):
        return u"Recent knowledge published by %s" % obj.username

    def items(self, obj):
        return Knowledge.objects.filter(user=obj).order_by('-created_datetime')[:30]


    def item_title(self, item):
        """
        Takes an item, as returned by items(), and returns the item's
        title as a normal Python string.
        """
        return item.question

    def item_author_name(self, item):
        """
        Takes an item, as returned by items(), and returns the item's
        author's name as a normal Python string.
        """
        return item.user.username

    def item_author_link(self, item):
        """
        Takes an item, as returned by items(), and returns the item's
        author's URL as a normal Python string.
        """
        current_site = Site.objects.get_current()
        return "http://%s%s" %(current_site.domain, item.user.get_absolute_url())

