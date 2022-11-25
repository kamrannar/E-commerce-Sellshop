from rest_framework import serializers
from accounts.models import *
from product.api.serializers import ProductVersionSerializer



class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')

class SubscriberEmailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Newsletter
        fields = ('email',)

class WishlistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Wishlist
        fields = '__all__'



class CartSerializer(serializers.ModelSerializer):
    user_id = UserSerializer()
    class Meta:
        model = Cart
        fields = '__all__'

class Cart_itemSerializer(serializers.ModelSerializer):
    product_version_id = ProductVersionSerializer()  
    cart_id = CartSerializer()  
    class Meta:
        model = Cart_item
        fields = '__all__'
    

class Cart_itemPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cart_item
        fields = '__all__'

class WishlistDetailedSerializer(serializers.ModelSerializer):
    product_version_id = ProductVersionSerializer()  
    class Meta:
        model = Wishlist
        fields = '__all__'