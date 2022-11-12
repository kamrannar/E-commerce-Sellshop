from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework import generics
from .serializers import *
from accounts.models import *
from accounts.api.serializers import CartSerializer, Cart_itemSerializer, Cart_itemPostSerializer
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import json
from rest_framework import status

class CartitemViewset(viewsets.ModelViewSet):
    queryset = Cart_item.objects.all()
    serializer_class = Cart_itemSerializer


class CartitemPostView(APIView):
    queryset = Cart_item.objects.all()
    def get(self,request,*args,**kwargs):
        cart_items = Cart_item.objects.all()
        serializer = Cart_itemPostSerializer(cart_items,many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = Cart_itemPostSerializer(data=request.data)
        data = json.loads(request.body)
        product_version_id = request.data.get('product_version_id')
        cart_id = request.data.get('cart_id')
        a = Cart_item.objects.filter(product_version_id=product_version_id,cart_id=cart_id).first()
        if a:
            if 'action' in data:
                action=data['action']
                if action=="increase":
                    a.quantity+=1
                    a.save()
                    if serializer.is_valid():
                        return Response(serializer.data)
                elif action=='decrease' and a.quantity==1:
                    a.delete()
                    if serializer.is_valid():
                        return Response(serializer.data)
                    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
                elif action=='decrease' :
                    a.quantity-=1
                    a.save()
                    if serializer.is_valid():
                        return Response(serializer.data)
            else:
                a.delete()
                if serializer.is_valid():
                    return Response(serializer.data)
                return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WishlistView(APIView):
    queryset = Wishlist.objects.all()

    def get(self,request,*args,**kwargs):
        cart_items = Wishlist.objects.all()
        serializer = WishlistSerializer(cart_items,many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = WishlistSerializer(data=request.data)
        product_version_id = request.data.get('product_version_id')
        user_id = request.data.get('user_id_wishlist')
        a = Wishlist.objects.filter(product_version_id=product_version_id,user_id_wishlist=user_id)
        if a:
            a.delete()
            if serializer.is_valid():
                return Response(serializer.data)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        else:
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)            



class CartViewset(viewsets.ModelViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializer


class MyTokenObtainPairSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['first_name'] = user.first_name

        return token


class MyTokenObtainPairView(TokenObtainPairView):
    serializer_class = MyTokenObtainPairSerializer

class SubscriberEmailView(generics.ListCreateAPIView):

    serializer_class = SubscriberEmailSerializer
    queryset = Newsletter.objects.all()


class UserView(generics.ListCreateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
