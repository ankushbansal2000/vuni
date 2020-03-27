from rest_framework import serializers
from .models import FeePattern
class FeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeePattern
        fields = "__all__"