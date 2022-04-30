from django import forms
from django.forms.widgets import Textarea, TextInput

from django_blog_example import models


class PostForm(forms.ModelForm):
    """Form to create a new blog post"""

    class Meta:
        model = models.Post
        exclude = ("id",)


class CommentForm(forms.ModelForm):
    """Form to create a new comment"""

    class Meta:
        model = models.Comment
        exclude = ("id",)
