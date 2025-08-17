from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()

class Post(models.Model):
    title = models.CharField(max_length=160)
    slug = models.SlugField(max_length=160, unique=True)
    excerpt = models.TextField(blank=True)
    content = models.TextField()
    cover_image = models.URLField(blank=True, null=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='posts')
    published = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['-published_at']

    def __str__(self):
        return self.title
    