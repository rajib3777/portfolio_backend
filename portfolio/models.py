from django.db import models

class HeroSection(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    subtitle =  models.CharField(max_length=300)
    profile_image = models.ImageField(upload_to='hero_images/')
    highligted_text = models.CharField(max_length=200)
    github_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    social_media_url = models.URLField(blank=True, null=True)
    
    def __str__(self):
        return self.name
    
    
class AboutSection(models.Model):
    short_bio = models.TextField()
    long_bio = models.TextField()
    location = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    year_of_experience = models.TextField()
    available_for_work = models.BooleanField(default=True)
    
    def __str__(self):
        return "About Section"
    
    
class SkillCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, related_name='skills', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    level = models.IntegerField(help_text="0-100 percentage")

    def __str__(self):
        return f"{self.name} ({self.level}%)"


class ProjectCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Project(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    category = models.ForeignKey(ProjectCategory, related_name='projects', on_delete=models.SET_NULL, null=True)
    description = models.TextField()
    tech_stack = models.CharField(max_length=255, help_text="Comma separated tech list")
    thumbnail = models.ImageField(upload_to='projects/')
    demo_link = models.URLField(blank=True)
    github_link = models.URLField(blank=True)
    featured = models.BooleanField(default=False)
    created_at = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.title


class Experience(models.Model):
    role = models.CharField(max_length=150)
    company = models.CharField(max_length=150)
    start_date = models.DateField()
    end_date = models.DateField(null=True, blank=True)
    is_current = models.BooleanField(default=False)
    description = models.TextField(blank=True)

    def __str__(self):
        return f"{self.role} @ {self.company}"


class Education(models.Model):
    institution = models.CharField(max_length=200)
    degree = models.CharField(max_length=200)
    start_year = models.IntegerField()
    end_year = models.IntegerField()
    description = models.TextField(blank=True)

    def __str__(self):
        return self.degree


class SocialLink(models.Model):
    platform = models.CharField(max_length=50)
    url = models.URLField()

    def __str__(self):
        return self.platform


class Stats(models.Model):
    total_projects = models.IntegerField(default=0)
    total_clients = models.IntegerField(default=0)
    total_awards = models.IntegerField(default=0)

    def __str__(self):
        return "Stats"

    
