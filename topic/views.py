from django.shortcuts import render, get_object_or_404
from django.views import View
from .models import Topic


class TopicList(View):

    def get(self, request, category, *args, **kwargs):

        queryset = Topic.objects.filter(category_id=1)
        topic = get_object_or_404(queryset)

        return render(
            request,
            "topic_detail.html",
            {
                "title": topic
            },
        )
