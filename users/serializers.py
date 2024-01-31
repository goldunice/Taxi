from rest_framework import serializers
from .models import *


class CustomOperatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username", "password"]


class CustomDriverSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username"]
