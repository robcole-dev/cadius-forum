from django.shortcuts import render, get_object_or_404
from django.views import View
from category.models import Category
from .models import Topic
from .forms import TopicForm


def topic_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    topics = Topic.objects.filter(category=category)
    template = "topic_detail.html"
    context = {
        "category": category,
        "topics": topics,
    }
    return render(request, template, context)


def new_topic(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    topics = Topic.objects.filter(category=category)
    template = "new_topic.html"
    context = {
        "category": category,
        "topics": topics,
        "topic_form": TopicForm(),
    }
    return render(request, template, context)
