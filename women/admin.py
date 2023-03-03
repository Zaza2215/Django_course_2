from django.contrib import admin
from django.utils.safestring import mark_safe

from women import models


# Register your models here.

class WomenAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "slug", "time_create", "get_html_photo", "is_published", "cat")
    list_display_links = ("id", "title")
    search_fields = ("title", "content")
    list_editable = ("is_published",)
    list_filter = ("is_published", "time_create")
    prepopulated_fields = {"slug": ("title",)}
    fields = ('title', 'slug', 'cat', 'content', 'photo', 'is_published', 'get_html_photo', 'time_create', 'time_update')
    readonly_fields = ('get_html_photo', 'time_create', 'time_update')
    save_on_top = True

    def get_html_photo(self, object):
        if object.photo:
            return mark_safe(f"<img src='{object.photo.url}' width=50>")

    get_html_photo.short_description = 'Miniature'


class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "slug")
    list_display_links = ("id", "name")
    search_fields = ("name",)
    prepopulated_fields = {"slug": ("name",)}


admin.site.register(models.Women, WomenAdmin)
admin.site.register(models.Category, CategoryAdmin)

admin.site.site_title = 'Django site admin URK'
admin.site.site_header = 'Django administration (URK)'
