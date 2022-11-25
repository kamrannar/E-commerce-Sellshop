from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenRefreshView, TokenBlacklistView
from accounts.api.views import CartViewset, CartitemViewset, CartitemPostView
from django.urls import path, include
from .views import *


router = DefaultRouter()

router.register(r'cart_items', CartitemViewset)
router.register(r'carts', CartViewset)

urlpatterns = [
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/blacklist/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('subscribe/', SubscriberEmailView.as_view(), name='subscribe'),
    path('users/', UserView.as_view(), name='users'),
    path('', include('rest_registration.api.urls')),
    path('', include(router.urls)),
    path('cartitems_post/', CartitemPostView.as_view(), name='cart_api'),
    path('wishlist/', WishlistView.as_view(), name='wishlist_api'),
    path('wishlist_detailed/', WishlistDetailedView.as_view(), name='wishlist_api'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

]
