from django import forms
from blog.models import Blog


class BlogF(forms.ModelForm):
    class Meta:
        model=Blog
        exclude=['summary','idenfier','user']

