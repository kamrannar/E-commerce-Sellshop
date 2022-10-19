from django.urls import path,include
from order.api.views import CartViewset,CartitemViewset

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'cart_items', CartitemViewset)
router.register(r'carts', CartViewset)

urlpatterns = [
    path('', include(router.urls)),
]
 