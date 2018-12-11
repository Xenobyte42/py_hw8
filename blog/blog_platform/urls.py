from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path('', views.MainPage.as_view(), name='main_page'),
    path('newpost/', views.NewPost.as_view(), name='new_post'),
    path('post/<str:post_name>/edit/', views.PostEdit.as_view(), name='post_edit'),
    path('post/<str:post_name>', views.PostView.as_view(), name='post'),
    path('theme/', views.PostTheme.as_view(), name='post_theme'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('register/', views.RegView.as_view(), name='register_page'),
]
