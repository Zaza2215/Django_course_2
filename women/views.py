from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseNotFound, Http404


# Create your views here.
def index(request):
    return HttpResponse('Page app women.')


def categories(request, category_id):
    if request.GET:
        print(request.GET)
    return HttpResponse(f'<h1>Category {category_id}</h1>')


def archive(request, year):
    if year > 2023:
        # Http404()
        return redirect('home', permanent=True)

    return HttpResponse(f'year: {year}')


def page_not_found(request, exception):
    return HttpResponseNotFound('<h1>Page was not found</h1>')
