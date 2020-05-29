from rest_framework import authentication
from users.models import Bankinfo
from .serializers import BankinfoSerializer
from rest_framework import viewsets


class BankinfoViewSet(viewsets.ModelViewSet):
    serializer_class = BankinfoSerializer
    authentication_classes = (
        authentication.SessionAuthentication,
        authentication.TokenAuthentication,
    )
    queryset = Bankinfo.objects.all()
