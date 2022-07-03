from django.contrib import admin
from .models import Topic


@admin.register()

class AdminTopic(admin.ModelAdmin):
    list_filter = ['category', 'title', 'author', 'closed']
    list_display = ['category', 'title', 'author', 'closed']
    search_fields = ['category', 'title', 'author']
