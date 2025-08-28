from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import *
from portfolio.models import Portfolio
from portfolio.serializer import PortfolioSerializer
from portfolio.permissions import IsAuthorOrReadOnly


# Portfolio View: List and create posts
class PortfolioList(ListCreateAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = [IsAuthorOrReadOnly]

    # If we didnt create this we need to pass the id which is insecure
    # Instead we attach the current user upon creation of the post
    # Its not automatically attached, so we must do this
    # def perform_create(self, serializer):
    #     serializer.save(author=self.request.user)

# Read, Update and Delete single post (requires login)
class PortfolioDetail(RetrieveUpdateDestroyAPIView):
    queryset = Portfolio.objects.all()
    serializer_class = PortfolioSerializer
    permission_classes = [IsAuthenticated, IsAuthorOrReadOnly]
    
