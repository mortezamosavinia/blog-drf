from django.urls import path,include
from rest_framework import routers
from app.api import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('blogapi', views.BlogViewset, basename='blog')

urlpatterns = [
    path('', include(router.urls))
]
