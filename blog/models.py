from django.db import models
from django.conf import settings


class Post(models.Model):
    """A blog post that is auto-created from Markdown input"""
    title = models.CharField(max_length=200, blank=True)
    author =  models.ForeignKey(to=settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    posted_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    raw_markdown = models.TextField(null=False, blank=False)
