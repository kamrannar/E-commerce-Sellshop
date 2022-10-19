from django.urls import path
from .views import call_heavy_process, single_product, product_listt,product_detail,product_list
from rest_framework.urlpatterns import format_suffix_patterns


urlpatterns = [
    path('product_list/', product_list.as_view(), name='product_list'),
    path('<slug:slug>/', single_product.as_view(), name='single_product'),
    path('a/', product_listt),
    path('a/<int:id>', product_detail),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)