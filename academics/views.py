from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .serializers import  BatchSerializer
from .models import Batch
# Create your views here.

class addBatch(ListCreateAPIView):
    serializer_class = BatchSerializer
    queryset = Batch.objects.all()
    