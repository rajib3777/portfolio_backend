from django.contrib import admin
from .models import BlogPost, BlogCategory

@admin.register(BlogPost)
class BlogPostAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "published_at")
    search_fields = ("title", "content")
    list_filter = ("category",)

admin.site.register(BlogCategory)