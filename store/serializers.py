from rest_framework import serializers
from .models import *

class CategorySeriaLizer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['category_name']

class ProductSeriaLizer(serializers.ModelSerializer):
    category = CategorySeriaLizer()
    created_date = serializers.DateTimeField(format='%d-%m-%Y %H:%M')
    class Meta:
        model = Product
        fields = ['id', 'product_name', 'description', 'category', 'price', 'have',
                  'image', 'video', 'created_date']