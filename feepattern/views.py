from rest_framework import generics
from .serializer import FeeSerializer,FeeHeadSerializer
from .models import FeePattern, FeePatternHead
from academics.models import Batch
from register.models import Student_Details
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
import json
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
    queryset = list(FeePattern.objects.all())
    l=[]
    for p in queryset:
        if str(p.fee_pattern_class_name)+"_"+p.fee_pattern_type+"_"+p.fee_pattern_batch in l:
            pass
        else:
            l.append(
                    str(p.fee_pattern_class_name)+"_"+p.fee_pattern_type+"_"+str(p.fee_pattern_batch),
            )
    return JsonResponse({'FeeName': l})
@csrf_exempt
@api_view(["POST"])
def feePay(request):
    if request.method=="POST":
        d={
            'payable' : request.data.get("amount"),
        'payment_mode' : request.data.get("payment_mode"),
        'cheque_no' : request.data.get("cheque_no"),
        }
        sid = request.data.get("id")        
        sdata = Student_Details.objects.get(id=sid)
        pre = (sdata.student_fee_deatils)
        from datetime import datetime
        from pytz import timezone    
        south_africa = timezone('Asia/Kolkata')
        sa_time = datetime.now(south_africa)
        time=(sa_time.strftime('%Y-%m-%d_%H-%M-%S'))
        if pre:
            pre[time]=d
        else:
            pre={}
            pre[time]=d

        sdata.student_fee_deatils = pre
        sdata.save()
        return Response({'data':"Payment Success"})

def studentsFeeDetails(request):
    sid = request.GET.get('id')
    data = Student_Details.objects.get(id = sid)
    batchData = data.student_batch.split("_")
    batch  = Batch.objects.get(batch=batchData[0],academic_year=batchData[1])
    print(batch.start_date)
    start = batch.start_date.split("-")
    end = batch.end_date.split("-")
    from datetime import datetime
    end_date = datetime(int(end[0]),int(end[1]),int(end[2]))
    start_date = datetime(int(start[0]),int(start[1]),int(start[2]))
    num_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
    print(num_months)

    month = 12

    print(data.student_fee_pattern)
    print(data.student_fee_deatils)
    feedata = FeePatternHead.objects.get(fee_pattern_name=data.student_fee_pattern)
    print(feedata)
    fee_collect_pattern = int(feedata.fee_collect_pattern)
    print(fee_collect_pattern)
    interval = month//int(fee_collect_pattern)
    res=[]
    interval=5
    from datetime import date 
    from datetime import timedelta 
    
    # Get today's date 
    today = date.today()
    today = date(int(end[0]),int(end[1]),int(end[2])) 
    print(type(today))
    print("Today is: ", today) 
    
    # Yesterday date 
    yesterday = today - timedelta(days = 1) 
    print("Yesterday was: ", yesterday) 
    for i in range(interval):
        res.append({'start':start[0]+"-"+str(start[1])+"-"+start[2]})

        start[1]=int(start[1])+fee_collect_pattern
        if(start[1]>12):
            start[1]-=12
            start[0]=str(int(start[0])+1)
    print(res)
    print(interval) 
    print(sid)

