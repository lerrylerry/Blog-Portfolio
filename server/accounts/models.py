from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from phonenumber_field.modelfields import PhoneNumberField

# This is a good practice when referencing to user model, it will always return the active user model
User = get_user_model()

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="author")
    bio = models.TextField(max_length=99, blank=True, null=True, default="No bio yet")
    birthdate = models.DateField(blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True, unique=True)
    picture = models.ImageField(upload_to="images/", blank=True, null=True)

    def __str__(self):
        return self.user.username