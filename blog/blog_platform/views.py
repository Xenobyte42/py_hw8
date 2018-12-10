from django.shortcuts import render
from django.shortcuts import redirect

from .models import *
from .forms import *


MAIN_HTML = 'main.html'
POST_HTML = 'post.html'
THEME_HTML = 'theme.html'
NEWPOST_HTML = 'add_post.html'


def main_page(request):
    if request.GET.get('viewsort', None):
        posts = Post.objects.view_sort()
    else:
        posts = Post.objects.date_sort()
    
    context = {'posts': posts}
    return render(request, MAIN_HTML, context)

def new_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()

            return redirect('post', post_name=post.theme)
    else:
        form = PostForm()
    
    context = {'form': form}
    return render(request, NEWPOST_HTML, context)

def post(request, post_name):
    post = Post.objects.get_post(post_name)
    context = {'post': post}
    return render(request, POST_HTML, context)

def post_theme(request, post_theme):
    return render(request, THEME_HTML)
