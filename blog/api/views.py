from blog.api.serializers import BlogSerializer
from blog.models import Blog
from rest_framework import viewsets
# from rest_framework import permissions

class BlogViewset(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [] 
