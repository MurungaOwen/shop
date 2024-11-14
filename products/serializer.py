from rest_framework.serializers import ModelSerializer
from .models import Product


class ProductSerializer(ModelSerializer):
    """serialize product to valid json"""
    class Meta:
        model = Product
        fields = "__all__"