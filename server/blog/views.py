from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import *
from blog.models import Blog
from blog.serializer import BlogSerializer
from blog.permissions import IsAuthorOrReadOnly


# Blog View: List and create posts
class BlogList(ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthorOrReadOnly]

    # If we didnt create this we need to pass the id which is insecure
    # Instead we attach the current user upon creation of the post
    # Its not automatically attached, so we must do this
    def perform_create(self, serializer):
        serializer.save(author=self.request.user)

# Read, Update and Delete single post (requires login)
class BlogDetail(RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    