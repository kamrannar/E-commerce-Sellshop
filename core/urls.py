from django.urls import path
from .views import home,about,ContactView,error,SearchResultsView
urlpatterns = [
    path('', home.as_view(), name='home'),
    path('about/', about, name='about'),
    path('contact/', ContactView.as_view(), name='contact'),
    path('404/', error, name='404'),
    path('search/', SearchResultsView.as_view(), name='search'),

]

