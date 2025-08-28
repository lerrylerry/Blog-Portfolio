from django.db import models
from django.contrib.auth import get_user_model

# This is a good practice when referencing to user model, it will always return the active user model
User = get_user_model()

class Tag(models.Model):
    name = models.CharField(max_length=99, unique=True)
    slug = models.SlugField(max_length=99, unique=True)

class Portfolio(models.Model):
    title = models.CharField(max_length=99)
    slug = models.SlugField(max_length=99, unique=True)
    description = models.TextField()
    link = models.URLField(blank=True, null=True)
    image = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    featured = models.BooleanField(default=False)
    tags = models.ManyToManyField(Tag, blank=True, related_name="projects")

    def __str__(self):
        return self.title
    
