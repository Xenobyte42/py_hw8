from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_page, name='main_page'),
    path('newpost/', views.new_post, name='new_post'),
    path('post/<str:post_name>', views.post, name='post'),
    path('theme/', views.post_theme, name='post_theme'),
]
