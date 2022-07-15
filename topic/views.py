from datetime import date
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from category.models import Category
from .models import Topic
from .forms import TopicForm


def category_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    topics = Topic.objects.filter(category=category)
    template = "topic/category_detail.html"
    context = {
        "category": category,
        "topics": topics,
    }
    return render(request, template, context)


@login_required
def new_topic(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    topic_form = TopicForm(request.POST or None)
    if request.method == 'POST':
        if topic_form.is_valid():
            topic_form.instance.author = request.user
            topic_form.instance.category = category
            topic = topic_form.save()
            topic_id = topic.pk
            messages.success(request, 'Topic Added')
            return redirect(reverse('topic_detail', args=[category_id, topic_id]))
        messages.error(request, "Try again!")

    template = "topic/new_topic.html"
    context = {
        "category": category,
        "topic_form": topic_form,
    }
    return render(request, template, context)


@login_required
def edit_topic(request, category_id, topic_id):
    category = get_object_or_404(Category, id=category_id)
    topic = get_object_or_404(Topic, id=topic_id)
    if topic.author != request.user:
        messages.error(request, "You are not the author!")
        return redirect('home')
    topic_form = TopicForm(request.POST or None, instance=topic)
    if request.method == 'POST':
        if topic_form.is_valid():
            topic_form.instance.author = request.user
            topic_form.instance.category = category
            topic_form.save()
            messages.success(request, 'Topic Updated')
            return redirect(reverse('topic_detail', args=[category_id, topic_id]))
        messages.error(request, "Try again!")

    template = "topic/edit_topic.html"
    context = {
        "category": category,
        "topic": topic,
        "topic_form": topic_form,
    }
    return render(request, template, context)


@login_required
def delete_topic(request, category_id, topic_id):
    category = get_object_or_404(Category, id=category_id)
    topic = get_object_or_404(Topic, id=topic_id)
    if topic.author != request.user:
        messages.error(request, "You are not the author!")
        return redirect('home')
    topic.delete()
    messages.success(request, 'Topic deleted')
    return redirect(reverse('category_detail', args=[category_id]))
