from django.db import models

# Create your models here.

class Category(models.Model):
    """
    Model for site Categories
    """
    name = models.CharField(max_length=50, unique=True)
