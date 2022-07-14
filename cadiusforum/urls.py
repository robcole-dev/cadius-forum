"""cadiusforum URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from category.views import CategoryList
from topic import views as topic_views
from reply import views as reply_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('allauth.urls')),
    path('', CategoryList.as_view(), name='home'),
    path('<int:category_id>/', topic_views.topic_detail, name="topics"),
    path('topic/new/<int:category_id>/', topic_views.new_topic, name="new_topic"),
    path('topics/<int:topic_id>/', reply_views.reply_detail, name="replys"),
]
