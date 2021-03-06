from django.db import models
from django.contrib.auth.models import User
from category.models import Category
from tinymce.models import HTMLField


class Topic(models.Model):
    """
    Model for user topics posts
    """
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=50, unique=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    startdate = models.DateTimeField(auto_now_add=True)
    closed = models.BooleanField(default=False)
    description = HTMLField(blank=True)

    class Meta:
        ordering = ['startdate']

    def __str__(self):
        return self.title
