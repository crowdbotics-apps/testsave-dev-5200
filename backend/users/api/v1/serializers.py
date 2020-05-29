from rest_framework import serializers
from users.models import Bankinfo


class BankinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bankinfo
        fields = "__all__"
