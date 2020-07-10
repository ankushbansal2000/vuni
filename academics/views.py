from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView,ListAPIView
from .serializers import  BatchSerializer,ExcelByBatchSerializer
from .models import Batch
from feepattern.models import FeePatternHead
from register.models import Student_Details
from django.http import JsonResponse,HttpResponse
import io
from xlsxwriter.workbook import Workbook
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
            str(p.batch)+"_"+p.academic_year
        )
    return JsonResponse({'batch':l})
from datetime import date
from datetime import timedelta
from dateutil.relativedelta import relativedelta

def excelByBatch(request):
    # serializer_class = ExcelByBatchSerializer
    # def get(self,request,*args, **kwargs):
        batch = request.GET.get('batch')
        data = Student_Details.objects.filter(student_batch=batch).values()
        # print(data)
        
        output = io.BytesIO()

        workbook = Workbook(output, {'in_memory': True})
        worksheet = workbook.add_worksheet()
        worksheet.write(0, 0,'Id')
        worksheet.write(0, 1,'Name')
        worksheet.write(0, 2,'Father Name')
        worksheet.write(0, 3,'Mobile No.')
        worksheet.write(0, 4,'Batch')

        worksheet.write(0, 5,'Pending')
        worksheet.write(0, 6,'Pay')
        for i in range(len(data)):
            feedata = FeePatternHead.objects.get(fee_pattern_name=data[i]['student_fee_pattern'])
            fee_collect_pattern = int(feedata.fee_collect_pattern)
            today = date.today()+relativedelta(months=+fee_collect_pattern)
            feeData = data[i]['student_fee_mont_wise']
            pending = 0
            pay = 0

            if feeData:
                res=feeData
                for m in res:
                    d = list(map(int,m['end'].split("-")))
                    if date(d[0],d[1],d[2])<today:
                        
                        pending+=m['feePending']
                        pay = m['feePaid']

            worksheet.write(i+1, 0,data[i]['id'])
            worksheet.write(i+1, 1,data[i]['student_name'])
            worksheet.write(i+1, 2,data[i]['student_father'])
            worksheet.write(i+1, 3,data[i]['student_ph'])
            worksheet.write(i+1, 4,data[i]['student_batch'])
            
            worksheet.write(i+1, 5,pending)
            worksheet.write(i+1, 6,pay)

            # worksheet.write(i, 2,data[i]['student_fee_mont_wise'])
            # print(data[i]['student_fee_mont_wise'])
        workbook.close()

        output.seek(0)
        response = HttpResponse(output.read(),content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
        response['Content-Disposition'] = 'attachment; filename=excel.xlsx'
        output.close()
        return response
        # return FileResponse(,as_attachment=False,filename="pdf.pdf")
