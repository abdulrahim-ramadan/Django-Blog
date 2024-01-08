from django import forms
from django_summernote.fields import SummernoteTextFormField
from .models import Post
from django_summernote.widgets import SummernoteWidget, SummernoteInplaceWidget


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        widgets = {
            'content': SummernoteWidget(),
            #'bar': SummernoteInplaceWidget(),
        }