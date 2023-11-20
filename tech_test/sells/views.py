from django.shortcuts import render
from sells.models import *
from rest_framework import generics, permissions
from .serializers import *
from rest_framework.response import Response
from rest_framework import status

# Create your views here.
class SellInOutListCreateView(generics.ListCreateAPIView):
    queryset = selling_in_out.objects.all()
    serializer_class = SellingInOutSerializer

class SellInOutGetDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = selling_in_out.objects.all()
    serializer_class = SellingInOutSerializer

class SellInListCreateView(generics.ListCreateAPIView):
    queryset = selling_in.objects.all()
    serializer_class = SellingInSerializer
    # def perform_create(self, serializer):
    #     sell_in_out = selling_in_out.objects.filter(user = self.request.data["user"], product = self.request.data["product"]).last()


class SellInGetDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = selling_in.objects.all()
    serializer_class = SellingInSerializer

class SellOutListCreateView(generics.ListCreateAPIView):
    queryset = selling_out.objects.all()
    serializer_class = SellingOutSerializer

class SellOutGetDeleteUpdateView(generics.RetrieveUpdateDestroyAPIView):
    queryset = selling_out.objects.all()
    serializer_class = SellingOutSerializer


