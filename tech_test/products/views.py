from django.shortcuts import render
from products.models import *
from rest_framework import generics, permissions
from .serializers import *
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class ProductListCreateView(generics.ListCreateAPIView):
    queryset = product.objects.all()
    serializer_class = ProductSerializer

class ProductGetDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = product.objects.all()
    serializer_class = ProductSerializer

