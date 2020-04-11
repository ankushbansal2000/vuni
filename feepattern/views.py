from rest_framework import generics
from .serializer import FeeSerializer
from .models import FeePattern
from rest_framework.exceptions import NotFound
# Create your views here.

class Fee(generics.ListCreateAPIView):
    serializer_class = FeeSerializer
    def get_queryset(self):
        if self.request.method == "POST":
            queryset = FeePattern.objects.all()
            return queryset
        elif self.request.method == "GET":
            queryset = FeePattern.objects.all()
            return queryset
        else:
            raise NotFound('method not allowed')
