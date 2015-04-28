from django.db import models
from django.contrib.auth.models import User

class Article(models.Model):
    title = models.CharField(max_length=255, unique=True)
    author = models.OneToOneField(User)
    url = models.URLField()
    active = models.BooleanField(default=True)
    decision = models.BooleanField()
    
    def __unicode__(self):
        return self.title
    
class Review(models.Model):
    reviewer = models.ForeignKey(User)
    article = models.ForeignKey(Article)
    text = models.TextField()
    url = models.URLField()
    decision = models.BooleanField()
    
    def __unicode__(self):
        return self.reviewer