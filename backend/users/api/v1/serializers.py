from rest_framework import serializers
from users.models import Address, Bankinfo


class BankinfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bankinfo
        fields = "__all__"


class AddressSerializer(serializers.ModelSerializer):
    class Meta:
        model = Address
        fields = "__all__"
