from django.urls import path
from .views import BlogListView, BlogDetailView, BlogCategoryListView

urlpatterns = [
    path("", BlogListView.as_view()),
    path("categories/", BlogCategoryListView.as_view()),
    path("<slug:slug>/", BlogDetailView.as_view()),
]

