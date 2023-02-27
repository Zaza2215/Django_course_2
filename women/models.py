import os
import datetime

from django.utils.text import slugify
from django.db import models
from django.urls import reverse


# Create your models here.

def get_image_upload_path(instance, filename):
    """Generate upload path for ImageField"""
    filename, ext = os.path.splitext(filename)
    slug = slugify(instance.slug)
    return f'photos/{datetime.datetime.today().strftime("%Y/%m")}/{slug}{ext}'


class Women(models.Model):
    title = models.CharField(max_length=48, verbose_name="name")
    slug = models.SlugField(max_length=48, unique=True, db_index=True, verbose_name="URL")
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to=get_image_upload_path, blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name="Category")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    class Meta:
        verbose_name = "Famous woman"
        verbose_name_plural = "Famous women"
        ordering = ["time_create", "title"]


class Category(models.Model):
    name = models.CharField(max_length=48, db_index=True, verbose_name="Category")
    slug = models.SlugField(max_length=48, unique=True, verbose_name="URL")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_slug': self.slug})
