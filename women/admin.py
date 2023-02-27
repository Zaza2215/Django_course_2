from django.contrib import admin
from women import models


# Register your models here.

class WomenAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "slug", "time_create", "photo", "is_published", "cat")
    list_display_links = ("id", "title")
    search_fields = ("title", "content")
    list_editable = ("is_published",)
    list_filter = ("is_published", "time_create")
    prepopulated_fields = {"slug": ("title",)}


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(models.Women, WomenAdmin)
admin.site.register(models.Category, CategoryAdmin)
