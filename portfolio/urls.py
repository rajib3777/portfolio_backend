from django.urls import path
from .views import (
    HeroDetailView, AboutDetailView, SkillCategoryListView,
    ProjectListView, ProjectDetailView, ExperienceListView,
    EducationListView, SocialLinkListView, StatsDetailView
)

urlpatterns = [
    path('hero/', HeroDetailView.as_view()),
    path('about/', AboutDetailView.as_view()),
    path('skills/', SkillCategoryListView.as_view()),
    path('projects/', ProjectListView.as_view()),
    path('projects/<slug:slug>/', ProjectDetailView.as_view()),
    path('experience/', ExperienceListView.as_view()),
    path('education/', EducationListView.as_view()),
    path('social-links/', SocialLinkListView.as_view()),
    path('stats/', StatsDetailView.as_view()),
]
