from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView
from .serializers import  BatchSerializer
from .models import Batch
from django.http import JsonResponse
# Create your views here.

class addBatch(ListCreateAPIView):
    serializer_class = BatchSerializer
    def get_queryset(self):
        queryset = Batch.objects.all()
        return queryset


def seebatch(request):
    
    queryset = list(Batch.objects.all())
    l=[]
    for p in queryset:
        l.append(
            str(p.batch)+"_"+p.academic_year+"_"+p.start_date+"_"+p.end_date
        )
    return JsonResponse({'batch':l})

    