from datetime import datetime
from django.shortcuts import render, get_object_or_404, redirect, reverse
from django.conf import settings
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from category.models import Category
from topic.models import Topic
from .models import Reply
from .forms import ReplyForm


def topic_detail(request, category_id, topic_id):
    category = get_object_or_404(Category, id=category_id)
    topic = get_object_or_404(Topic, id=topic_id)
    replys = Reply.objects.filter(topic=topic)
    reply_form = ReplyForm(request.POST or None)
    if request.method == 'POST':
        if reply_form.is_valid():
            reply_form.instance.author = request.user
            reply_form.instance.category = category
            reply_form.instance.topic = topic
            reply_form.save()
            messages.success(request, "Reply Added")
            return redirect(reverse(
                'topic_detail', args=[category_id, topic_id]))
        messages.error(request, "Try again!")

    template = "reply/topic_detail.html"
    context = {
        "category_id": category_id,
        "category": category,
        "topic": topic,
        "replys": replys,
        "reply_form": reply_form,
        "TINYMCE_API": settings.TINYMCE_API,
    }
    return render(request, template, context)


@login_required
def edit_reply(request, category_id, topic_id, reply_id):
    category = get_object_or_404(Category, id=category_id)
    topic = get_object_or_404(Topic, id=topic_id)
    replys = Reply.objects.filter(topic=topic)
    reply = get_object_or_404(Reply, id=reply_id)
    if reply.author != request.user:
        messages.error(request, "You are not the Author!")
        return redirect('home')
    reply_form = ReplyForm(request.POST or None, instance=reply)
    if request.method == 'POST':
        if reply_form.is_valid():
            reply_form.instance.author = request.user
            reply_form.instance.category = category
            reply_form.instance.topic = topic
            reply_form.save()
            messages.success(request, "Reply updated")
            return redirect(reverse(
                'topic_detail', args=[category_id, topic_id]))
        messages.error(request, "Try again!")

    template = "reply/topic_detail.html"
    context = {
        "category_id": category_id,
        "category": category,
        "topic": topic,
        "replys": replys,
        "reply_form": reply_form,
        "TINYMCE_API": settings.TINYMCE_API,
    }
    return render(request, template, context)
