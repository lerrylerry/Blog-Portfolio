from django.db import models
from django.contrib.auth import get_user_model

# This is a good practice when referencing to user model, it will always return the active user model
User = get_user_model()

class Category(models.Model):
    name = models.CharField(max_length=99, unique=True)
    slug = models.SlugField(max_length=99, unique=True)

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=99, unique=True)
    slug = models.SlugField(max_length=99, unique=True)

    def __str__(self):
        return self.name

class Blog(models.Model):
    class Status(models.TextChoices):
        DRAFT = 'draft','Draft'
        PUBLISHED = 'published','Published'
        ARCHIVED = 'archived','Archived'
        PENDING = 'pending','Pending'

    title = models.CharField(max_length=99)
    slug = models.SlugField(max_length=99, unique=True)
    excerpt = models.TextField(blank=True)
    content = models.TextField()
    cover_image = models.URLField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=10, choices=Status.choices, default=Status.DRAFT)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="posts")
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name="blogs")
    tags = models.ManyToManyField(Tag, blank=True, related_name="blogs")

    class Meta:
        ordering = ["-updated_at"]

    def __str__(self):
        return f'{self.title} by: {self.author}'

