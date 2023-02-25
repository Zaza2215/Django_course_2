from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect

from .models import *


def index(request):
    posts = Women.objects.all()

    context = {
        'posts': posts,
        'title': 'Main page',
        'cat_selected': 0,
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


def show_category(request, cat_id):
    posts = Women.objects.filter(cat_id=cat_id)

    if len(posts) == 0:
        raise Http404()

    title = Category.objects.get(id=cat_id).name

    context = {
        'posts': posts,
        'title': f'view by {title}',
        'cat_selected': cat_id,
    }
    return render(request, 'women/index.html', context=context)
