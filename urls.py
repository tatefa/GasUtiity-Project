# api/urls.py
from django.urls import path
from .views import UserViewSet, ComplaintViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
router.register(r'complaints', ComplaintViewSet, basename='complaint')

urlpatterns = router.urls
