from django.db import models
from django.contrib.auth.models import User
from topic.models import Topic
from tinymce.models import HTMLField


class Reply(models.Model):
    """
    Model for Topic replys
    """
    topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
    description = HTMLField(blank=True)
    author = models.ForeignKey(User, on_delete=models.DO_NOTHING)
    replydate = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['replydate']

    def __str__(self):
        return self.description
