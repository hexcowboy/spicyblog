import markdown
from django.conf import settings
from django.db import models


class Post(models.Model):
    """A blog post that is auto-created from Markdown input"""
    title = models.CharField(max_length=200, blank=True)
    author = models.ForeignKey(to=settings.AUTH_USER_MODEL,
                               on_delete=models.CASCADE)
    posted_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    body = models.TextField()
    body_rendered = models.TextField(blank=True)

    def save(self, *args, **kwargs):
        self.body_rendered = markdown.markdown(
            self.body, extensions=['codehilite', 'fenced_code'])
        super().save(*args, **kwargs)

    def __str__(self):
        """Use the title as the representation"""
        return self.title

    class Meta:
        ordering = ('-posted_date', )
