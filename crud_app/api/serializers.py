from rest_framework import serializers
from .models import ProductItem, UserAccount
from rest_framework.validators import UniqueValidator


class ProductItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductItem
        fields = ['id', 'name', 'title', 'price', 'image', 'date_added']


class UserAccountSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserAccount
        fields = ['id', 'name', 'email']
