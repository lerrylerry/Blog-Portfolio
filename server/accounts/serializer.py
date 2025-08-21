from rest_framework.serializers import ModelSerializer
from django.contrib.auth.models import User
from accounts.models import Profile

class ProfileSerializer(ModelSerializer):
    class Meta:
        model = Profile
        fields = "__all__"

class RegisterSerializer(ModelSerializer):

    class Meta:
        model = User
        fields = ("username","email","password")
        extra_kwargs = {
            "password": {"write_only":True},
        }

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)#Dictionary unpacking
        Profile.objects.create(user=user)
        return user