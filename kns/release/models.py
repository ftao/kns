from django.db import models

class Release(models.Model):
    name =  models.CharField(max_length = 50, db_index = True)
    appid = models.CharField(max_length = 100)
    version = models.CharField(max_length = 30)
    url = models.URLField(max_length = 255)
    released_time = models.DateTimeField(auto_now_add = True)
    changelog = models.TextField()

