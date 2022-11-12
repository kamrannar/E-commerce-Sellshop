from django.urls import path,include
from order import views
urlpatterns = [

    path('order_complete/', views.order_complete, name='order_complete'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('paypal/', include('paypal.standard.ipn.urls')),
]
