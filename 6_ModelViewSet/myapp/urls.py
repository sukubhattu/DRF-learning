from django.db import router
from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('post', PostModelViewSet, basename='post')
router.register('postR', PostModelReadOnlyViewSet, basename='postR')

urlpatterns = [path('', include(router.urls))]
