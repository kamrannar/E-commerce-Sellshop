from order.api.serializers import CartSerializer,Cart_itemSerializer
from order.models import Cart_items,Cart
from rest_framework import viewsets

class CartitemViewset(viewsets.ModelViewSet):
    queryset = Cart_items.objects.all()
    serializer_class = Cart_itemSerializer

class CartViewset(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer
