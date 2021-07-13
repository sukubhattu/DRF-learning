from .models import Post
from .serializers import PostSerializer

from rest_framework import viewsets


class PostModelViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


# readonly action
class PostModelReadOnlyViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
