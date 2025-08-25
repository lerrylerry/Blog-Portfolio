from rest_framework import generics, permissions
from rest_framework.response import Response
from rest_framework.views import APIView
from django.contrib.auth.models import User
from accounts.serializer import ProfileSerializer, RegisterSerializer, CheckViewDetails

# Register view
class RegisterView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

# Profile view (requires login)
class ProfileView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        serializer = ProfileSerializer(request.user)
        return Response(serializer.data)

# Get some details temporarily
class GetDetails(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = CheckViewDetails