from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.conf import settings

class APIToken(models.Model):
    user = models.ForeignKey(User, unique = True)
    token = models.CharField(max_length = 50, unique = True)

    def __unicode__(self):
        return u'<user=%s, token=%s>' %(self.user.username, self.token)

    @staticmethod
    def get_user_token(user):
        return APIToken.objects.get(user = user).token

def create_api_token(sender, instance, created, **kwargs):
    if created:
        import hashlib,time
        token = hashlib.md5('%s%s%f' %(instance.username.encode('utf-8'), settings.SECRET_KEY, time.time())).hexdigest()
        APIToken.objects.create(user = instance, token = token)

post_save.connect(create_api_token, sender=User)
