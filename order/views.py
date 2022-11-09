from django.shortcuts import render


def order_complete(request):
    return render(request, 'order-complete.html')



def wishlist(request):
    return render(request, 'wishlist.html')


