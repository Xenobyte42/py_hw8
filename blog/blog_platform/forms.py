from django import forms

from .models import Post, Comment, BlogUser


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('theme', 'description', 'text',)


class CommentForm(forms.ModelForm):

    class Meta:
        model = Comment
        fields = ('text',)

class RegistrationForm(forms.ModelForm):

    class Meta:
        model = BlogUser
        fields = ('username', 'password', 'avatar', 'label',)
