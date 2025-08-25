from django.contrib import admin
from django.urls import path, include
from accounts.views import RegisterView, ProfileView, GetDetails
from blog.views import BlogList, BlogDetail
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),

    # Accounts URLS
    path("api/accounts/register/", RegisterView.as_view(), name="account-register"),
    path("api/accounts/login/", TokenObtainPairView.as_view(), name="account-login"),
    path("api/accounts/token/refresh/", TokenRefreshView.as_view(), name="account-token-refresh"),
    path("api/accounts/profile/", ProfileView.as_view(), name="account-profile"),
    path("api/accounts/<int:pk>/", GetDetails.as_view(), name="account-detail"),  # consider renaming later
    

    # Blog URLS
    path("api/blogs/", BlogList.as_view(), name="blog-list"),
    path("api/blogs/<int:pk>/", BlogDetail.as_view(), name="blog-detail"),
]
