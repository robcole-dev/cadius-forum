from django.contrib import admin
from .models import Reply


@admin.register(Reply)
class ReplyAdmin(admin.ModelAdmin):
    """
    Settings for filter, display and search
    """
    list_filter = ['topic', 'author', 'replydate']
    list_display = ['topic', 'author', 'replydate']
    search_fields = ['topic', 'author']
