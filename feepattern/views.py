from rest_framework import generics
from .serializer import FeeSerializer,FeeHeadSerializer
from .models import FeePattern, FeePatternHead
from register.models import Student_Details
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from django.http import JsonResponse
# Create your views here.

class Fee(generics.ListCreateAPIView):
    serializer_class = FeeSerializer
    def get_queryset(self):
        if self.request.method == "POST":
            queryset = FeePattern.objects.get()
            # for p in FeePattern.objects.raw("SELECT feepattern_FeePattern"):
            #     print(p.fee_pattern_type)
            return queryset
        elif self.request.method == "GET":
            queryset = FeePattern.objects.all()
            return queryset
            # return queryset


class FeeHead(generics.ListCreateAPIView):
    serializer_class = FeeHeadSerializer
    def get_queryset(self):
        if self.request.method == "GET":
            queryset = FeePatternHead.objects.all()
            return queryset
        if self.request.method == "POST":
            queryset = FeePatternHead.objects.all()
            return Response({'data': 'submitted successfully'})
            
    
def seefee(request):
    queryset = FeePattern.objects.all()
    l=[]
    for p in queryset.raw('SELECT * from feepattern_FeePattern'):
        if str(p.fee_pattern_class_name)+"_"+p.fee_pattern_type+"_"+p.fee_pattern_batch in l:
            pass
        else:
            l.append(
                    str(p.fee_pattern_class_name)+"_"+p.fee_pattern_type+"_"+str(p.fee_pattern_batch),
            )
    return JsonResponse({'FeeName': l})

def studentsFeeDetails(request):
    sid = request.GET.get('id')
    data = Student_Details.objects.get(id = sid)
    print(data.student_batch)
    print(data.student_fee_pattern)
    feedata = FeePatternHead.objects.get(fee_pattern_name=data.student_batch)
    fee_collect_pattern = (feedata.fee_collect_pattern)
    
    print(sid)

