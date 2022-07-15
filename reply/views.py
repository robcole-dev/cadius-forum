from django.shortcuts import render, get_object_or_404
from django.views import View
from topic.models import Topic
from .models import Reply
from .forms import ReplyForm


def topic_detail(request, category_id, topic_id):
    topic = get_object_or_404(Topic, id=topic_id)
    replys = Reply.objects.filter(topic=topic)
    template = "reply/topic_reply.html"
    context = {
        "category_id": category_id,
        "topic": topic,
        "replys": replys,
        "reply_form": ReplyForm(),
    }
    return render(request, template, context)
