from app.models import Blog
from app.api.serializers import BlogSerializer
from rest_framework import viewsets

class BlogViewset (viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer

# we can also add authentication to this api