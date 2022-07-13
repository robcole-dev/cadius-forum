from django import forms
from tinymce.widgets import TinyMCE
from .models import Topic


class TopicForm(forms.ModelForm):
    """
        Form to allow admins to manage Topics.
    """
    title = forms.CharField()
    description = forms.CharField(widget=TinyMCE(attrs={}))

    class Meta:
        model = Topic
        fields = "__all__"
