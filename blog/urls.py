from django.urls import path
from .views import *
        
urlpatterns = [
        path('blog/', BlogList.as_view(), name='blog'),
        path('blog/<str:slug>/', BlogDetail.as_view(), name='single_blog')
]