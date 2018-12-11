from django.shortcuts import render
from django.shortcuts import redirect
from django.core.paginator import Paginator
from django.contrib import auth
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views import View

from .models import Post, Comment, BlogUser
from .forms import PostForm, CommentForm, RegistrationForm
from blog import settings


def paginate(objects, request, amount):
    paginator = Paginator(objects, amount)
    page = request.GET.get('page')
    return paginator.get_page(page)


class MainPage(View):
    template_name = 'main.html'

    def get(self, request):
        user = request.user.is_authenticated and request.user.is_active
        if request.GET.get('viewsort', None):
            posts = Post.objects.view_sort()
        else:
            posts = Post.objects.date_sort()

        render_posts = paginate(posts, request, settings.POST_PER_PAGE)
        context = {'posts': render_posts, 'user': user}
        return render(request, self.template_name, context)


class NewPost(View):
    form_class = PostForm
    template_name = 'add_post.html'

    @method_decorator(login_required)
    def get(self, request):
        user = request.user.is_authenticated and request.user.is_active
        form = self.form_class()
        context = {'form': form, 'user': user}
        return render(request, self.template_name, context)

    @method_decorator(login_required)
    def post(self, request):
        user = request.user.is_authenticated and request.user.is_active
        form = self.form_class(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()

            return redirect('post', post_name=post.theme)
        context = {'form': form, 'user': user}
        return render(request, self.template_name, context)


class PostView(View):
    template_name = 'post.html'
    form_class = CommentForm

    def get(self, request, post_name):
        post = Post.objects.get_post(post_name)
        comments = Comment.objects.get_comments(post)
        render_comments = paginate(comments, request, settings.COMM_PER_PAGE)
        user = request.user.is_authenticated and request.user.is_active
        form = self.form_class()
        post.view_num += 1
        post.save()
        context = {'post': post, 'comments': render_comments, 'form': form, 'user': user}
        return render(request, self.template_name, context)

    def post(self, request, post_name):
        post = Post.objects.get_post(post_name)
        comments = Comment.objects.get_comments(post)
        render_comments = paginate(comments, request, settings.COMM_PER_PAGE)
        user = request.user.is_authenticated and request.user.is_active
        form = self.form_class(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.blog = rpost
            comment.save()

            return redirect('post', post_name=post.theme)
        context = {'post': post, 'comments': render_comments, 'form': form, 'user': user}
        return render(request, self.template_name, context)


class PostTheme(View):
    template_name = 'theme.html'

    def post(self, request):
        user = request.user.is_authenticated and request.user.is_active
        theme = request.POST.get('theme', None)
        posts = Post.objects.get_post_with(theme)

        render_posts = paginate(posts, request, settings.POST_PER_PAGE)
        context = {'theme': theme, 'posts': render_posts, 'user': user}
        return render(request, self.template_name, context)


class PostEdit(View):
    template_name = 'edit_post.html'
    form_class = PostForm

    @method_decorator(login_required)
    def get(self, request, post_name):
        user = request.user.is_authenticated and request.user.is_active
        post = Post.objects.get_post(post_name)
        form = self.form_class(instance=post)

        context = {'form': form, 'user': user}
        return render(request, self.template_name, context)

    @method_decorator(login_required)
    def post(self, request, post_name):
        user = request.user.is_authenticated and request.user.is_active
        post = Post.objects.get_post(post_name)
        form = self.form_class(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post', post_name=post.theme)
        context = {'post': post, 'comments': render_comments, 'form': form, 'user': user}
        return render(request, self.template_name, context)


class RegView(View):
    template_name = 'registration.html'
    form_class = RegistrationForm

    def get(self, request):
        user = request.user.is_authenticated and request.user.is_active
        form = self.form_class()
        context = {'form': form, 'user': user}
        return render(request, self.template_name, context)

    def post(self, request):
        user = request.user.is_authenticated and request.user.is_active
        form = self.form_class(request.POST, request.FILES)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('main_page')
        context = {'form': form, 'user': user}
        return render(request, self.template_name, context)

