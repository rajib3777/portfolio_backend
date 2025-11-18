from rest_framework import serializers
from .models import BlogPost, BlogCategory

class BlogCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogCategory
        fields = "__all__"


class BlogPostSerializer(serializers.ModelSerializer):
    category = BlogCategorySerializer(read_only=True)

    class Meta:
        model = BlogPost
        fields = "__all__"

