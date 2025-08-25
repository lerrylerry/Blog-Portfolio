from django.db import models
from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from blog.models import Blog

# Serialize
class BlogSerializer(ModelSerializer):
    # We use this to access the username and use instead of the ID for security purposes
    author = serializers.SlugRelatedField(
        read_only = True,
        slug_field = "username" # could be email
    )
    class Meta:
        model = Blog
        fields = [
            "id", "author", "title", "slug", "excerpt", "content", "cover_image", "created_at", "updated_at", "category", "tags"
        ]
