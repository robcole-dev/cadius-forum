from django.shortcuts import render, get_list_or_404
from django.views import View
from topic.models import Topic
from .models import Reply


def reply_detail(request, topic_id):
    topic = get_list_or_404(Topic, id=topic_id)
    replys = Reply.objects.filter(topic=topic)
    template = "topic_reply.html"
    context = {
        "topics": topic,
        "replys": replys,
    }
    return render(request, template, context)
