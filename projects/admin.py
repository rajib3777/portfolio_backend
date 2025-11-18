from django.contrib import admin
from .models import Project, ProjectCategory, ProjectImage

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "category", "created_at", "featured")
    list_filter = ("category", "featured")
    search_fields = ("title", "description")
    prepopulated_fields = {"slug": ("title",)}
    inlines = [ProjectImageInline]

admin.site.register(ProjectCategory)