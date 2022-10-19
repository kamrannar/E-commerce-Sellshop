from django.urls import path
from order import views
urlpatterns = [

    path('order_complete/', views.order_complete, name='order_complete'),
    path('wishlist/', views.wishlist, name='wishlist'),
    path('cart/', views.cart, name='cart')
]
