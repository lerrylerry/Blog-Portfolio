from django.db import models

class Project(models.Model):
    title = models.CharField(max_length=160)
    slug = models.SlugField(max_length=160, unique=True)
    description = models.TextField(blank=True)
    url = models.URLField(blank=True, null=True)
    image = models.URLField(blank=True, null=True)
    tags = models.CharField(max_length=200, blank=True)
    featured = models.BooleanField(default=False)

    def __str__(self):
        return self.title