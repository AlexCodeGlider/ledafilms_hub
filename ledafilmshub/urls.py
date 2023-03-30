from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import viewsets

router = DefaultRouter()
router.register(r'contracts', viewsets.ContractViewSet, basename='contract')
router.register(r'windows', viewsets.WindowViewSet, basename='window')
router.register(r'titles', viewsets.TitleViewSet, basename='title')

urlpatterns = [
    path('', include(router.urls)),
]
