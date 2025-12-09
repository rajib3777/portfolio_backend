from django.db import models
from django.utils.text import slugify
from cloudinary.models import CloudinaryField

class ProjectCategory(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True, blank=True)
    category = models.ForeignKey(ProjectCategory, related_name="projects",
                                 on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    tech_stack = models.CharField(max_length=255)
    thumbnail = CloudinaryField('image', folder='media/project_thumbnails', null=True, blank=True)
    github_link = models.URLField(blank=True, null=True)
    live_demo = models.URLField(blank=True, null=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return self.title


class ProjectImage(models.Model):
    project = models.ForeignKey(Project, related_name="images", on_delete=models.CASCADE)
    image = CloudinaryField('image', folder='media/project_images', null=True, blank=True)

    def __str__(self):
        return f"Image for {self.project.title}"
