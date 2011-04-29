from django.db import models
from django.contrib.auth.models import User

class APIToken(models.Model):
    user = models.ForeignKey(User)
    token = models.CharField(max_length = 50, unique = True)

    def __unicode__(self):
        return u'<user=%s, token=%s>' %(self.user.username, self.token)
