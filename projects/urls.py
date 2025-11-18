from django.urls import path
from .views import (
    ProjectListView, ProjectDetailView, ProjectCategoryListView,
)

urlpatterns = [
    path("", ProjectListView.as_view()),
    path("categories/", ProjectCategoryListView.as_view()),
    path("<slug:slug>/", ProjectDetailView.as_view()),
]

