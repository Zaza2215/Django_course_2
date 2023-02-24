from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *

menu = [
    {"title": "About", "url_name": "about"},
    {"title": "Add article", "url_name": "add-article"},
    {"title": "Feedback", "url_name": "contact"},
    {"title": "Sing in", "url_name": "login"},
]


def index(request):
    posts = Women.objects.all()
    context = {
        'posts': posts,
        'menu': menu,
        'title': 'Main page',
    }
    return render(request, 'women/index.html', context=context)


def about(request):
    context = {
        'menu': menu,
        'title': 'About site',
    }
    return render(request, 'women/about.html', context=context)


def addpage(request):
    return HttpResponse("Adding article")


def contact(request):
    return HttpResponse("Feedback")


def login(request):
    return HttpResponse("Log in")


def show_post(request, post_id: int):
    return HttpResponse(f'Post with id: {post_id}')


def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=False)

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')
