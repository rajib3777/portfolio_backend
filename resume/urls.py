from django.urls import path
from .views import dynamic_resume

urlpatterns = [
    path("dynamic/", dynamic_resume),
]

