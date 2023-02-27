from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404

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
        'title': 'About site',
    }
    return render(request, 'women/about.html', context=context)


def addpage(request):
    return HttpResponse("Adding article")


def contact(request):
    return HttpResponse("Feedback")


def login(request):
    return HttpResponse("Log in")


def show_post(request, post_slug):
    post = get_object_or_404(Women, slug=post_slug)

    context = {
        "post": post,
        "title": post.title,
        "cat_selected": post.cat_id,
    }

    return render(request, "women/post.html", context=context)


def archive(request, year):
    if int(year) > 2020:
        return redirect('home', permanent=False)

    return HttpResponse(f"<h1>Архив по годам</h1><p>{year}</p>")


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def show_category(request, cat_slug):
    posts = Women.objects.filter(cat_id=Category.objects.get(slug=cat_slug).pk)

    if len(posts) == 0:
        raise Http404()

    title = Category.objects.get(slug=cat_slug).name

    context = {
        'posts': posts,
        'title': f'view by {title}',
        'cat_selected': cat_slug,
    }
    return render(request, 'women/index.html', context=context)
