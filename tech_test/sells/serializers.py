from rest_framework import serializers
from .models import *

class SellingInOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = selling_in_out
        fields = '__all__'

class SellingInSerializer(serializers.ModelSerializer):
    class Meta:
        model = selling_in
        fields = '__all__'

class SellingOutSerializer(serializers.ModelSerializer):
    class Meta:
        model = selling_out
        fields = '__all__'

