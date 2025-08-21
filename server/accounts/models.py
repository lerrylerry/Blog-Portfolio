from django.db import models
from django.contrib.auth.models import User
from phonenumber_field.modelfields import PhoneNumberField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=99, blank=True, null=True, default="No bio yet")
    birthdate = models.DateField(blank=True, null=True)
    phone_number = PhoneNumberField(blank=True, null=True, unique=True)
    picture = models.ImageField(upload_to="images/", blank=True, null=True)


    def __str__(self):
        return self.user.username