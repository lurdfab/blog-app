from django.contrib import admin
from .models import Blog

# Register your models here.


class BlogAdmin(admin.ModelAdmin):
    list_display = ("id", "author", "title", "publication_date", "updated_at")


admin.site.register(Blog, BlogAdmin)