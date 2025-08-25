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
        fields = ["username","email","password"]
        extra_kwargs = {
            "password": {"write_only":True},
        }

    def create(self, validated_data):
        #Dictionary unpacking: Shortcut, Advanced Python Stuff
        user = User.objects.create_user(**validated_data)

        """
        # This is the equivalent code under the hood, the manual creation

        user = User.objects.create_user(
        username=validated_data["username"],
        password=validated_data["password"],
        email=validated_data["email"]
        )
        """

        Profile.objects.create(user=user)
        return user
    
class CheckViewDetails(ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"
