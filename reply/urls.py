from django.urls import path
from . import views

urlpatterns = [
    path(
        'category/<int:category_id>/topic/<int:topic_id>/',
        views.topic_detail, name="topic_detail"),
]
