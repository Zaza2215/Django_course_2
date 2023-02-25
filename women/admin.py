from django.contrib import admin
from women import models


# Register your models here.

class WomenAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "time_create", "photo", "is_published", "cat")
    list_display_links = ("id", "title")
    search_fields = ("title", "content")
    list_editable = ("is_published",)
    list_filter = ("is_published", "time_create")


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name")
    list_display_links = ("id", "name")
    search_fields = ("name",)


admin.site.register(models.Women, WomenAdmin)
admin.site.register(models.Category, CategoryAdmin)
