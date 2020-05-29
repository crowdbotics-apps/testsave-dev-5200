from rest_framework import authentication
from users.models import Address, Bankinfo
from .serializers import AddressSerializer, BankinfoSerializer
from rest_framework import viewsets


class BankinfoViewSet(viewsets.ModelViewSet):
    serializer_class = BankinfoSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Bankinfo.objects.all()


class AddressViewSet(viewsets.ModelViewSet):
    serializer_class = AddressSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Address.objects.all()
