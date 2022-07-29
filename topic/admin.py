from django.contrib import admin
from .models import Topic


@admin.register(Topic)
class TopicAdmin(admin.ModelAdmin):
    """
    Admin grid views for topic model
    """
    list_filter = ['category', 'title', 'author', 'closed']
    list_display = ['category', 'title', 'author', 'closed']
    search_fields = ['category', 'title', 'author']
