from rest_framework import serializers
from .models import *


class OperatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operator
        fields = "__all__"


class ClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Client
        fields = "__all__"


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = "__all__"
        extra_kwargs = {
            "driver": {"read_only": True},
            "status": {"read_only": True},
            "grade": {"read_only": True},
            "waiting_seconds": {"read_only": True},
            "total_sum": {"read_only": True},
        }
