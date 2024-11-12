from django.shortcuts import render
from rest_framework import generics
from .models import Product
from .serializer import ProductSerializer
from django_filters import rest_framework as filters

class ProductFilter(filters.FilterSet):
    name = filters.CharFilter(lookup_expr='icontains')
    category = filters.CharFilter(lookup_expr='icontains')
    class Meta:
        model = Product
        fields = ['name', 'category']

class ProductListing(generics.ListAPIView):
    """display all products in db"""
    lookup_field = "name"
    serializer_class = ProductSerializer
    queryset = Product.objects.all()
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = ProductFilter
