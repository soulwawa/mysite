from django import forms
from .models import Post
from markdownx.fields import MarkdownxFormField


class PostForm(forms.ModelForm):
    contents = MarkdownxFormField()

    class Meta:
        model = Post