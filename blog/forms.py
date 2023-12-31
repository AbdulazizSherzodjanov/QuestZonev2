from django import forms
from django.forms import ModelForm

from .models import PostModel,Comment


class PostModelForm(forms.ModelForm):
    content = forms.CharField(widget=forms.Textarea(attrs={'row': 4}))
    class Meta:
        model = PostModel
        fields = ['title','content']
        


class PostUpdateForm(forms.ModelForm):
    class Meta:
        model = PostModel
        fields = ('title','content')

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)







