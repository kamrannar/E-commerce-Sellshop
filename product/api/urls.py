from django.urls import path,include
from .views import *

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'categories', CategotyViewset)
router.register(r'product_list_api', ProductListViewset,basename="productlist_api")
router.register(r'product_version', ProductVersionViewset,basename="productversion_api")
router.register(r'colors', ColorViewset,basename="colors_api")
router.register(r'sizes', SizeViewset,basename="sizes_api")

urlpatterns = [
    path('', include(router.urls)),
]
