from django import forms
from tinymce.widgets import TinyMCE
from .models import Topic


class TopicForm(forms.ModelForm):
    """
        Form to allow Topics to be created or edited.
    """
    title = forms.CharField()
    description = forms.CharField(widget=TinyMCE(attrs={}))

    class Meta:
        model = Topic
        fields = (
            "title",
            "description",
        )
