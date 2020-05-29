from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import BankinfoViewSet

router = DefaultRouter()
router.register("bankinfo", BankinfoViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
