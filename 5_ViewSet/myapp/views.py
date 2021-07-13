from .serializers import PostSerializer
from .models import Post

from rest_framework import serializers, status
from rest_framework import viewsets
from rest_framework.response import Response


class PostViewSet(viewsets.ViewSet):
    def list(self, request):
        post = Post.objects.all()
        serializer = PostSerializer(post, many=True)
        return Response(serializer.data)

    def retrive(self, request, pk=None):
        if pk is not None:
            post = Post.objects.get(id=pk)
            serializer = PostSerializer(post)
            return Response(serializer.data)

    def create(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)
