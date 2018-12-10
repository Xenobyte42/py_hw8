from django.db import models


class Post(models.Model):
    theme = models.CharField(max_length=100, unique=True, verbose_name='Post theme')
    description = models.CharField(max_length=50, verbose_name='Description', default="")
    text = models.CharField(max_length=400, verbose_name='Post sample')
    is_active = models.BooleanField(default=True)
    view_num = models.BigIntegerField(default=0, verbose_name='Number of views')
    creation_time = models.DateTimeField('Date published', auto_now_add=True)


class Comment(models.Model):
    text = models.CharField(max_length=200, verbose_name='Comment sample')
    blog = models.ForeignKey(to='Post', on_delete=models.SET_NULL, null=True)

