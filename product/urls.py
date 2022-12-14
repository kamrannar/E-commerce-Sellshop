from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('<slug:slug>/', SingleProductView.as_view(), name='single_product'),
    ]

urlpatterns = format_suffix_patterns(urlpatterns)