from django.core.checks import messages
from django.http import response
from django.shortcuts import render
from rest_framework.serializers import Serializer
from .serializers import PostSerializer
from .models import Post


from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


@api_view(['GET', 'POST'])
def post_list(request):
    if request.method == "GET":
        posts = Post.objects.all()
        messages = {'msg': 'Just trying out custom message'}
        serializer = PostSerializer(posts, many=True)
        return Response({'messages': messages, 'data': serializer.data}, status=status.HTTP_200_OK)
    elif request.method == "POST":
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def post_detail(request, pk):
    try:
        post = Post.objects.get(id=pk)
    except Post.DoesNotExist:
        return Response({'msg': 'content not found'}, status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = PostSerializer(post)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PostSerializer(post, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg': 'Updated successfully', 'data': serializer.data}, status=status.HTTP_202_ACCEPTED)
        return Response({'msg': 'Error while updating'}, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
