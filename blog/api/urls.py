from django.urls import path,include
from blog.api.views import BlogViewset

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register(r'blogs', BlogViewset)

urlpatterns = [
    path('', include(router.urls)),
]
 