from rest_framework import serializers
from product.models import *
class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['id','title']

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = '__all__'

class ProductVersionSerializer(serializers.ModelSerializer):

    color_id = ColorSerializer() 
    size_id =  SizeSerializer()
    class Meta:
        model = Product_version
        fields = '__all__'