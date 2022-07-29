from django.shortcuts import render
from django.views import generic
from .models import Category


class CategoryList(generic.ListView):
    """
    Views for category app
    """
    model = Category
    template_name = "index.html"
