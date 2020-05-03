from rest_framework import generics
from .serializer import FeeSerializer,FeeHeadSerializer
from .models import FeePattern, FeePatternHead
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
# Create your views here.

class Fee(generics.ListCreateAPIView):
    serializer_class = FeeSerializer
    def get_queryset(self):
        if self.request.method == "POST":
            queryset = FeePattern.objects.get()
            # for p in FeePattern.objects.raw():
            #     print(p)
            return queryset
        elif self.request.method == "GET":
            queryset = FeePattern.objects.all()
            for p in FeePattern.objects.raw('SELECT id, fee_pattern_class_name FROM feepattern_FeePattern'):
                print('a')
                print(p)
            return queryset


class FeeHead(generics.ListCreateAPIView):
    serializer_class = FeeHeadSerializer
    def get_queryset(self):
        if self.request.method == "GET":
            queryset = FeePatternHead.objects.all()
            return queryset
        if self.request.method == "POST":
            queryset = FeePatternHead.objects.all()
            return Response({'data': 'submitted successfully'})
            
    
