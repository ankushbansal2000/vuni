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
        data = sdata.student_fee_mont_wise
                
        i =0
        paid = int(d['payable'])
        n = len(data)
        from datetime import datetime
        from pytz import timezone    
        south_africa = timezone('Asia/Kolkata')
        sa_time = datetime.now(south_africa)
        time=(sa_time.strftime('%Y-%m-%d_%H-%M-%S'))
        while(i<n):
            if data[i]['status'] == 'pending' :
                if data[i]['feePending'] == paid:
                    data[i]['feePending'] -= paid
                    data[i]['feePaid'] += paid
                    paid = 0
                    data[i]['status'] = 'paid'
                    data[i]['trnc']=time
                    break
                elif data[i]['feePending'] > paid:
                    
                    data[i]['feePending'] -= paid
                    data[i]['feePaid'] += paid
                    paid = 0
                    data[i]['trnc']=time
                    break
                else :
                    while(i<n and paid -  data[i]['feePending'] >0 ):
                        temp = data[i]['feePending']
                        data[i]['feePaid'] += temp
                        data[i]['feePending'] = 0
                        data[i]['status'] = 'paid'
                        paid -= temp
                        data[i]['trnc']=time
                        i+=1
                        
            else :
                i+=1
        if pre:
            pre[time]=d
        else:
            pre={}
            pre[time]=d

        sdata.student_fee_deatils = pre
        sdata.save()
        sdata.student_fee_mont_wise=data
        sdata.save()
        
        return Response({'data':"Payment Success"})

def studentsFeeDetails(request):
    sid = request.GET.get('id')
    data = Student_Details.objects.get(id = sid)
    batchData = data.student_batch.split("_")
    try:
        batch  = Batch.objects.get(batch=batchData[0],academic_year=batchData[1])
    except:
        return JsonResponse({'error':"Batch Not Assigned"})
    start = batch.start_date
    end = batch.end_date
    month = 12
    feedata = FeePatternHead.objects.get(fee_pattern_name=data.student_fee_pattern)
    fee_collect_pattern = int(feedata.fee_collect_pattern)
    interval = month//int(fee_collect_pattern)
    total_fee = int(feedata.total_academic_fee)+int(feedata.total_tution_fee)+int(feedata.total_hostel_fee)
    res=[]
    from datetime import date
    from datetime import timedelta
    from dateutil.relativedelta import relativedelta
    today = date.today()+relativedelta(months=+fee_collect_pattern)
    feeData = data.student_fee_mont_wise
    c=0
    if feeData:
        res=feeData
        for i in res:
            d = list(map(int,i['end'].split("-")))
            if date(d[0],d[1],d[2])<today and i['status']=="pending":
                i['status']="selected"
                c+=i['feePending']
    else:
        for i in range(interval):
            next = start+relativedelta(months=+fee_collect_pattern)
            res.append({'start':start,'end':next-timedelta(days=1),'status':"pending","feePending":total_fee,"feePaid":0})
            start=next
        data.student_fee_mont_wise = res
        data.save()
        for i in res:
            if i['end']<today and i['status']=="pending":
                i['status']="selected"
                c+=i['feePending']
    amount = c
    return JsonResponse({'amount':amount,'monthly_data':res})
