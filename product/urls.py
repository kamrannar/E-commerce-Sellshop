from django.urls import path
from .views import *
from rest_framework.urlpatterns import format_suffix_patterns
from sellshop.tasks import heavy_process

urlpatterns = [
    path('product_list/', ProductListView.as_view(), name='product_list'),
    path('<slug:slug>/', SingleProductView.as_view(), name='single_product'),
    path('a/', product_listt),
    path('a/<int:id>', product_detail),
    path('call_heavy_process',call_heavy_process,name='call_heavy_process')
    ]

urlpatterns = format_suffix_patterns(urlpatterns)