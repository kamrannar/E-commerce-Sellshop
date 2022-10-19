from django.shortcuts import render
import json
from django.http import JsonResponse
from order.models import Cart_items
from product.models import Product



def order_complete(request):
    return render(request, 'order-complete.html')



def wishlist(request):
    return render(request, 'wishlist.html')


def cart(request):
    return render(request, 'cart.html')

