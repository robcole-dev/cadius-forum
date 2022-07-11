from django.shortcuts import render, get_object_or_404
from django.views import View
from category.models import Category
from .models import Topic


# class TopicList(View):

#     def get(self, request, category, *args, **kwargs):

#         queryset = Topic.objects.filter(category=category)
#         topic = get_object_or_404(queryset)

#         return render(
#             request,
#             "topic_detail.html",
#             {
#                 "title": topic
#             },
#         )


def topic_detail(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    topics = Topic.objects.filter(category=category)
    template = "topic_detail.html"
    context = {
        "category": category,
        "topics": topics,
    }
    return render(request, template, context)
