from django.contrib import admin
from django.urls import path, include
from category.views import CategoryList

urlpatterns = [
    path('admin/', admin.site.urls),
    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('allauth.urls')),
    path('', CategoryList.as_view(), name='home'),
    path('topics/', include('topic.urls')),
    path('replys/', include('reply.urls')),
]
