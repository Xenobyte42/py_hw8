from django.shortcuts import render
from django.http import HttpResponse


def main_page(request):
    return HttpResponse("Main")

def new_post(request):
    return HttpResponse("New post")

def post(request, post_name):
    return HttpResponse("Post")

def post_theme(request, post_theme):
    return HttpResponse("Post theme")
