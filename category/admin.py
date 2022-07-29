from django.contrib import admin
from .models import Category


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    """
    Admin grid views for category model
    """
    list_filter = ['name']
    list_display = ['name']
    search_fields = ['name']
