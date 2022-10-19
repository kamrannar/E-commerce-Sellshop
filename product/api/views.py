from product.api.serializers import *
from product.models import *
from rest_framework import viewsets


class CategotyViewset(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = []


class ProductVersionViewset(viewsets.ModelViewSet):
    queryset = Product_version.objects.all()
    serializer_class = ProductVersionSerializer
    permission_classes = []


class ProductListViewset(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = []


class ColorViewset(viewsets.ModelViewSet):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    permission_classes = []


class SizeViewset(viewsets.ModelViewSet):
    queryset = Size.objects.all()
    serializer_class = SizeSerializer
    permission_classes = []
