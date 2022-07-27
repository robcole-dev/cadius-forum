from django.urls import path, include
from . import views
from topic import views as topicviews
from topic import urls

urlpatterns = [
    path(
        'category/<int:category_id>/',
        topicviews.category_detail, name="category_detail"),
    path(
        'category/<int:category_id>/topic/<int:topic_id>/',
        views.topic_detail, name="topic_detail"),
    path(
        'edit/category/<int:category_id>/topic/<int:topic_id>/reply/<int:reply_id>',  # noqa
        views.edit_reply, name="edit_reply"),
]
