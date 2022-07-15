from django.urls import path
from . import views

urlpatterns = [
    path(
        'category/<int:category_id>/',
        views.category_detail, name="category_detail"),
    path('new/<int:category_id>/', views.new_topic, name="new_topic"),
    path(
        'edit/category/<int:category_id>/topic/<int:topic_id>/',
        views.edit_topic, name="edit_topic"),
    path(
        'delete/category/<int:category_id>/topic/<int:topic_id>/',
        views.delete_topic, name="delete_topic"),
]
