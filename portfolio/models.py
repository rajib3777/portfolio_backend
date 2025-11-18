from django.db import models

class HeroSection(models.Model):
    name = models.CharField(max_length=100)
    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=300, blank=True, null=True)
    profile_image = models.ImageField(upload_to="hero_images/", blank=True, null=True)
    highlighted_text = models.CharField(max_length=200, blank=True, null=True)
    github_url = models.URLField(blank=True, null=True)
    linkedin_url = models.URLField(blank=True, null=True)
    social_media_url = models.URLField(blank=True, null=True)

    def __str__(self):
        return self.name


class AboutSection(models.Model):
    short_bio = models.TextField()
    long_bio = models.TextField(blank=True, null=True)
    location = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    year_of_experience = models.IntegerField()
    available_for_work = models.BooleanField(default=True)

    def __str__(self):
        return "About Section"


class SkillCategory(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Skill(models.Model):
    category = models.ForeignKey(SkillCategory, related_name="skills", on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    level = models.IntegerField(help_text="0–100 percentage")

    def __str__(self):
        return f"{self.name} ({self.level}%)"


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