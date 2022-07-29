from .models import Reply
from django import forms
from tinymce.widgets import TinyMCE


class ReplyForm(forms.ModelForm):
    """
    Form for the Reply App
    """
    description = forms.CharField(widget=TinyMCE(attrs={}))

    class Meta:
        model = Reply
        fields = ('description',)
