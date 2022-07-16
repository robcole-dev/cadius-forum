from django.urls import path
from . import views

urlpatterns = [
    path(
        'category/<int:category_id>/topic/<int:topic_id>/',
        views.topic_detail, name="topic_detail"),
    path(
        'edit/category/<int:category_id>/topic/<int:topic_id>/reply/<int:reply_id>',  # noqa
        views.edit_reply, name="edit_reply"),
]
