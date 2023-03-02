from django import template
from women import models
from django.db.models import Count

register = template.Library()


@register.simple_tag(name='get_categories')
def get_categories_all(filter_cats=None):
    if filter_cats:
        return models.Category.objects.filter(pk=filter_cats)
    else:
        return models.Category.objects.all()


@register.inclusion_tag("women/list_categories.html")
def show_categories(sort_cats=None, cat_selected=0):
    if sort_cats:
        cats = models.Category.objects.annotate(total=Count('get_posts')).order_by(sort_cats)
    else:
        cats = models.Category.objects.annotate(total=Count('get_posts'))
    return {"cats": cats, "cat_selected": cat_selected}


@register.inclusion_tag("women/menu.html")
def show_menu(user):
    menu = [
        {"title": "About", "url_name": "about"},
        {"title": "Add article", "url_name": "add-article"},
        {"title": "Feedback", "url_name": "contact"},
    ]
    return {"menu": menu, "user": user}
