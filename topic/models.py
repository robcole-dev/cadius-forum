from django.db import models
from django.contrib.auth.models import User
import category

STATUS = ((0, 'Draft'), (1, 'Published'))

class Topic(models.Model):
    """
    Model for user topics posts
    """
    category = models.ForeignKey(category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    startdate = models.DateTimeField(auto_now_add=True)
    closed = models.BooleanField(default=False)
    description = models.TextField(blank=True)
