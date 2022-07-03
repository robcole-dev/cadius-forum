from django.db import models
from django.contrib.auth.models import User
import topic


class Reply(models.Model):
    """
    Model for Topic replys
    """
    topic = models.ForeignKey(topic, on_delete=models.CASCADE)
    description = models.TextField(blank=True)
    author = models.ForeignKey(User, on_delete=None)
    replydate = models.DateTimeField(auto_now_add=True)