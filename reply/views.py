from django.shortcuts import render, get_list_or_404
from django.views import View
from category.models import Category
from topic.models import Topic
from .models import Reply


def reply_detail(request, category_id, topic_id):
    category = get_list_or_404(Category, id1=category_id)
    topic = get_list_or_404(Topic, id2=topic_id)
    replys = Reply.objects.filter(topic=topic)
    template = "topic_reply.html"
    context = {
        "category": category,
        "topic": topic,
        "replys": replys,
    }
    return render(request, template, context)
