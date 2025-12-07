from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserChangeForm
from .models import Post, Comment
from taggit.forms import TagWidget

class ProfileUpdateForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
        widgets = {
            'tags': TagWidget(),  # makes tag input easy to manage
        }

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
