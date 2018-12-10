from django.shortcuts import render
from .models import *


MAIN_HTML = 'main.html'
POST_HTML = 'post.html'
THEME_HTML = 'theme.html'
NEWPOST_HTML = 'add_post.html'


def main_page(request):
    posts = Post.objects.all()
    
    context = {'posts': posts}
    return render(request, MAIN_HTML, context)

def new_post(request):
    return render(request, NEWPOST_HTML)

def post(request, post_name):
    post = Post.objects.all()[0]
    context = {'post': post}
    return render(request, POST_HTML, context)

def post_theme(request, post_theme):
    return render(request, THEME_HTML)
