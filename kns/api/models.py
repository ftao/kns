from django.db import models
from django.contrib.auth.models import User

class APIToken(models.Model):
    user = models.ForeignKey(User)
    token = models.CharField(max_length = 50)

