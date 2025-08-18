from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from blog.views import PostList, PostViewSet, PostDetail
from blog import views
from portfolio.views import ProjectViewSet
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView


router = DefaultRouter()
router.register("posts", PostViewSet, basename="posts")
router.register("projects", ProjectViewSet, basename="projects")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),


    path('posts/', views.PostList.as_view()),
    path('posts/<int:pk>/', views.PostDetail.as_view()),
    path('posts/create/', views.PostCreate.as_view()),

    
    # path("api/auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    # path("api/auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
]
