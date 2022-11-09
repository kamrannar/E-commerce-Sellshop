from rest_framework import serializers
from product.models import *

class SubcategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    subcategories = SubcategorySerializer()
    class Meta:
        model = Category
        fields = '__all__'


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    product_size = SizeSerializer(many=True)
    product_color = ColorSerializer(many=True)
    class Meta:
        model = Product
        fields = '__all__'


class ProductVersionSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    color_id = ColorSerializer()
    size_id = SizeSerializer(many=True)

    class Meta:
        model = Product_version
        fields = '__all__'
