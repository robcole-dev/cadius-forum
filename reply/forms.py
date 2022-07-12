from .models import Reply
from django import forms
from tinymce import models as tinymce_models


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ('description',)
