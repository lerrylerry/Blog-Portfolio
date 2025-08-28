from django.contrib import admin
from django.urls import path, include
from accounts.views import RegisterView, ProfileView, GetDetails
from blog.views import BlogList, BlogDetail
from portfolio.views import PortfolioList, PortfolioDetail
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path("admin/", admin.site.urls),

    # Accounts URLs
    path("api/accounts/register/", RegisterView.as_view(), name="account-register"),
    path("api/accounts/login/", TokenObtainPairView.as_view(), name="account-login"),
    path("api/accounts/token/refresh/", TokenRefreshView.as_view(), name="account-token-refresh"),
    path("api/accounts/profile/", ProfileView.as_view(), name="account-profile"),
    path("api/accounts/<int:pk>/", GetDetails.as_view(), name="account-detail"),  # consider renaming later
    

    # Blog URLs
    path("api/blogs/", BlogList.as_view(), name="blog-list"),
    path("api/blogs/<int:pk>/", BlogDetail.as_view(), name="blog-detail"),

    # Portfolio URLs
    path("api/portfolio/", PortfolioList.as_view(), name="portfolio-list"),
    path("api/portfolio/<int:pk>/", PortfolioDetail.as_view(), name="portfolio-detail"),
    
]
