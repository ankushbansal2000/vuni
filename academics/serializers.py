from rest_framework.serializers import ModelSerializer,Serializer
from .models import Batch

class BatchSerializer(ModelSerializer):
    class Meta:
        model = Batch
        fields = "__all__"

class ExcelByBatchSerializer(Serializer):
    class Meta:
        fields = None