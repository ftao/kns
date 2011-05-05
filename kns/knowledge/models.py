from django.db import models
from django.contrib.auth.models import User

class Knowledge(models.Model):
    user = models.ForeignKey(User)
    question = models.CharField(max_length = 500)
    search_keywords = models.CharField(max_length = 500, blank = True)
    answer_page_link = models.URLField(max_length = 500, verify_exists = False, blank = True)
    answer_page_title = models.CharField(max_length = 500, blank = True)
    answer_summary = models.TextField(blank = True)
    tags = models.CharField(max_length = 500, blank = True)
    created_datetime = models.DateTimeField(auto_now_add = True)


    def __unicode__(self):
        return self.question

    @models.permalink
    def get_absolute_url(self):
        return ('knowledge_detail', (), {
            'object_id': self.id
        })

    def _get_taglist(self):
        return [x for x in self.tags.split(u',') if x ]
        
    taglist = property(_get_taglist)
        
    class Meta:
        ordering = ['-created_datetime']
