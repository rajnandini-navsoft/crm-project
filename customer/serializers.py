from rest_framework import serializers
from .models import *





class ProductSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('category', 'slug', 'name', 'image', "description")

class CustomerSerializer(serializers.ModelSerializer):

    class Meta:
        model = CustomerAdd 
        fields = '__all__'

class ReviewSerializer(serializers.ModelSerializer):
    class Meta:
        model = Review
        fields = '__all__'

class CustomerAddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomerAddress
        fields = '__all__'

class StateSerilaizer(serializers.ModelSerializer):
    class Meta:
        model=State
        fields ='__all__'


