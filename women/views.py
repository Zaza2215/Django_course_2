from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404
from .models import *

# Create your views here.
menu = ['About', 'Add article', 'Feedback', 'Log in']


def index(request):
    posts = Women.objects.all()
    context = {
        'menu': menu,
        'posts': posts,
        'title': 'Main page',
    }
    return render(request, 'women/index.html', context=context)


def about(request):
    context = {
        'menu': menu,
        'title': 'About',
    }
    return render(request, 'women/about.html', context=context)


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page was not found</h1>')
