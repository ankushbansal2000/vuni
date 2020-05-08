from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .serializers import  BatchSerializer
from .models import Batch
# Create your views here.

class addBatch(ListCreateAPIView):
    serializer_class = BatchSerializer
    def get_queryset(self):
        queryset = Batch.objects.all()
        l=[]
        for p in queryset.raw("SELECT * from academics_Batch"):
            l.append(
                p.batch+"_"+p.academic_year+"_"+p.staet_date+"_"+p.end_date
            )
        queryset = l
        return queryset

    