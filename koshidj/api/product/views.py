from django.shortcuts import render
from .serializer import ProductSerializer
from .models import Product
from rest_framework import serializers, viewsets

class ProductViewSet(viewsets.ModelViewSet):
    queryset=Product.objects.all().order_by('id')
    serializer_class=ProductSerializer