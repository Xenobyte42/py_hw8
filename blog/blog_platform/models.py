from django.db import models
from django.shortcuts import get_object_or_404


class PostManager(models.Manager):

    def view_sort(self):
        return self.filter(is_active=True).order_by('-view_num')

    def date_sort(self):
        return self.filter(is_active=True).order_by('-creation_time')

    def get_post(self, post_name):
        post = get_object_or_404(Post, theme=post_name)
        return post


class CommentManager(models.Manager):

    def get_comments(self, post):
        return post.comment.all()


class Post(models.Model):
    objects = PostManager()

    theme = models.CharField(max_length=100, unique=True, verbose_name='Post theme')
    description = models.CharField(max_length=50, verbose_name='Description', default="")
    text = models.TextField(max_length=400, verbose_name='Post sample')
    is_active = models.BooleanField(default=True)
    view_num = models.BigIntegerField(default=0, verbose_name='Number of views')
    creation_time = models.DateTimeField('Date published', auto_now_add=True)


class Comment(models.Model):
    objects = CommentManager()
    
    text = models.TextField(max_length=200, verbose_name='')
    blog = models.ForeignKey(to='Post', on_delete=models.SET_NULL, null=True, related_name='comment')

