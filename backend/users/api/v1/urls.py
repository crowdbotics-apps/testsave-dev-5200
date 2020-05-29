from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import AddressViewSet, BankinfoViewSet

router = DefaultRouter()
router.register("bankinfo", BankinfoViewSet)
router.register("address", AddressViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
