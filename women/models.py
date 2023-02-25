from django.db import models
from django.urls import reverse


# Create your models here.

class Women(models.Model):
    title = models.CharField(max_length=48, verbose_name="name")
    content = models.TextField(blank=True)
    photo = models.ImageField(upload_to='photos/%Y/%m/%d/', blank=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    is_published = models.BooleanField(default=True)
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, null=True, verbose_name="Category")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_id': self.pk})

    class Meta:
        verbose_name = "Famous woman"
        verbose_name_plural = "Famous women"
        ordering = ["time_create", "title"]


class Category(models.Model):
    name = models.CharField(max_length=48, db_index=True, verbose_name="Category")

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'cat_id': self.pk})
