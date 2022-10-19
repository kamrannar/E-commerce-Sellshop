from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
from django.urls import path,include
from .views import *
from rest_framework_simplejwt.views import TokenBlacklistView
urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('subscribe/', SubscriberEmailView.as_view(), name='subscribe'),
    path('users/', UserView.as_view(), name='users'),
    path('', include('rest_registration.api.urls')),
]
