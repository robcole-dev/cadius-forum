from django.db import models


class Category(models.Model):
    """
    Model for site Categories
    """
    name = models.CharField(max_length=50, unique=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['name']
