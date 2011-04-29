from django.db import models
from django.contrib.auth.models import User

class Knowledge(models.Model):
    user = models.ForeignKey(User)
    question = models.CharField(max_length = 1000)
    answer_page_link = models.URLField(max_length = 500)
    answer_page_title = models.CharField(max_length = 500)
    answer_summary = models.CharField(max_length = 2000, blank = True)
    tags = models.CharField(max_length = 500, blank = True)
    created_datetime = models.DateTimeField(auto_now_add = True)

