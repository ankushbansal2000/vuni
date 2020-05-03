from rest_framework import serializers
from .models import FeePattern,FeePatternHead

class FeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeePattern
        fields = "__all__"


class FeeHeadSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeePatternHead
        fields = "__all__"
