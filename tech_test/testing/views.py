from django.shortcuts import render
from testing.models import *
from rest_framework import generics, permissions
from .serializers import *
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class TestListCreateView(generics.ListCreateAPIView):
    queryset = testing.objects.all()
    serializer_class = TestSerializer

class TestGetDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = testing.objects.all()
    serializer_class = TestSerializer

