from django.shortcuts import render
from django.shortcuts import redirect
from django.core.paginator import Paginator

from .models import *
from .forms import *


MAIN_HTML = 'main.html'
POST_HTML = 'post.html'
THEME_HTML = 'theme.html'
NEWPOST_HTML = 'add_post.html'
EDITPOST_HTML = 'edit_post.html'
POST_PER_PAGE = 4
COMM_PER_PAGE = 10


def paginate(objects, request, amount):
    paginator = Paginator(objects, amount)
    page = request.GET.get('page')
    return paginator.get_page(page)

def main_page(request):
    if request.GET.get('viewsort', None):
        posts = Post.objects.view_sort()
    else:
        posts = Post.objects.date_sort()

    render_posts = paginate(posts, request, POST_PER_PAGE)
    context = {'posts': render_posts}
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

    comments = Comment.objects.get_comments(post)
    render_comments = paginate(comments, request, COMM_PER_PAGE)

    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = post
            comment.save()
            
            return redirect('post', post_name=post_name)
    else:
        form = CommentForm()
    post.view_num += 1
    post.save()
    context = {'post': post, 'comments': render_comments, 'form': form}
    return render(request, POST_HTML, context)

def post_theme(request):
    theme = request.POST.get('theme', None)
    posts = Post.objects.get_post_with(theme)

    render_posts = paginate(posts, request, POST_PER_PAGE)
    context = {'theme': theme, 'posts': render_posts}
    return render(request, THEME_HTML, context)

def post_edit(request, post_name):
    post = Post.objects.get_post(post_name)

    if request.method == 'POST':
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.save()
            return redirect('post', post_name=post.theme)
    else:
        form = PostForm(instance=post)
    context = {'form': form}
    return render(request, EDITPOST_HTML, context)
    

