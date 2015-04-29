from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify

class Article(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, unique=True)
    author = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(default="Enter text here")
    active = models.BooleanField(default=True)
    decision = models.NullBooleanField(null=True)
    slug = models.SlugField(default='',unique = True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Article, self).save(*args, **kwargs)
    
    def __unicode__(self):
        return self.title
    
class Review(models.Model):
    id = models.AutoField(primary_key=True)
    reviewer = models.ForeignKey(User)
    article = models.ForeignKey(Article)
    date = models.DateTimeField(auto_now_add=True)
    text = models.TextField(default="Enter text here")
    decision = models.NullBooleanField(null=True)
    
    def __unicode__(self):
        return self.text