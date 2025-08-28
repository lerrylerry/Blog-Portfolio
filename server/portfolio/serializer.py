from rest_framework.serializers import ModelSerializer
from portfolio.models import Portfolio

# Serialize
class PortfolioSerializer(ModelSerializer):
    class Meta:
        model = Portfolio
        fields = ["id", "title", "slug", "description", "link", "image", "created_at", "updated_at", "featured", "tags"]
