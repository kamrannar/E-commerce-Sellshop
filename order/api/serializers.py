from rest_framework import serializers
from order.models import Cart_items,Cart
from product.api.serializers import ProductVersionSerializer
from accounts.api.serializers import UserSerializer 


class CartSerializer(serializers.ModelSerializer):
    user_id = UserSerializer()
    class Meta:
        model = Cart
        fields = '__all__'

class Cart_itemSerializer(serializers.ModelSerializer):
    product_version_id = ProductVersionSerializer()  
    cart_id = CartSerializer()  
    class Meta:
        model = Cart_items
        fields = '__all__'