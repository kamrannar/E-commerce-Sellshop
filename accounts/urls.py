from django.urls import path

from .views import MyAccount,checkout,RegisterView,CartView,WishlistView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import *
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='registration/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='registration/logout.html'), name='logout'),
    path('my_account/', login_required(MyAccount.as_view(template_name='my-account.html')), name='my_account'),
    path('wishlist/', login_required(WishlistView.as_view(template_name='wishlist.html')), name='wishlist'),
    path('checkout/', checkout, name='checkout'),
    path('change-password/', auth_views.PasswordChangeView.as_view()),
    path('register/', RegisterView.as_view(template_name = 'registration/register.html'), name='register'),
    path('cart/', CartView.as_view(), name='cart'),

]
 