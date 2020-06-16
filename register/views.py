from .models import Student_Details,Student_Image
from rest_framework import generics,filters,viewsets
from .serializer import StudentSerializers,StudentGet,StudentUpdate,StudentImage
from rest_framework.exceptions import MethodNotAllowed
from django.views.decorators.csrf import csrf_exempt
from django.http import JsonResponse
from feepattern.models import *
from rest_framework.response import Response
class StudentViewSet(generics.ListCreateAPIView):
    def get_serializer_class(self):
        if self.request.method == "POST":
            serializer_class = StudentSerializers
            return serializer_class
        elif self.request.method == "GET":
            serializer_class = StudentGet
            return serializer_class
        else:
            raise MethodNotAllowed
    def get_queryset(self):
        if self.request.method == 'POST':
            queryset = Student_Details.objects.all()
            return queryset
        elif self.request.method == 'GET':
            queryset = Student_Details.objects.all()
            return queryset
        else:
            raise MethodNotAllowed

class SearchStudent(generics.ListAPIView):
    queryset = Student_Details.objects.all()
    serializer_class = StudentSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['student_name','id']

class StudentRegistrationUpdate(generics.CreateAPIView):
    queryset = Student_Details.objects.all()
    serializer_class = StudentUpdate
    def post(self, request, *args, **kwargs):               #save user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        batch = request.data['student_batch']
        print(batch)
        idd = request.GET.get('id')
        student = Student_Details.objects.get(id=idd)
        sBatch=student.student_batch
        if sBatch=='':
            batchYear = batch.split('_')[1]
            feepattern = student.student_course+"_"+student.student_category+"_"+batchYear
            try:
                fee = FeePattern.objects.get(fee_pattern_class_name=student.student_course,fee_pattern_type=student.student_category,fee_pattern_batch=batchYear)
            except:
                return Response({'error':"Batch not assigned, Please add a feepattern with class: "+student.student_course+" , type: "+student.student_category+" , batch: "+batchYear+" and then add a feehead with feepattern:  "+feepattern})
            try:
                FeePatternHead.objects.get(fee_pattern_name = feepattern)
            except:
                return Response({'error':"Batch not assigned, Please add a feehead with feepattern:  "+feepattern})
            student.student_batch=batch
            student.student_fee_pattern=feepattern
            student.save()
            return Response({'success':"Batch Assigned SuccessFully"})
        else:
            return Response({'error':"Batch Already Assigned"})


        # serializer.save()
        # try:
        #     admin = Admin.objects.get(username = username)
        #     return Response({'error': 'user with this username already exist'})
        # except:
        #     try:
        #         admin = Admin.objects.get(email = username)
        #         return Response({'error': 'user with this email already exist'})
        #     except:
        #         user = serializer.save()
        #         response = Response({
        #             "success": "user has been successfully register",
        #         })
        #         return response
    
        
        


class ImageViewSet(viewsets.ModelViewSet):
    queryset = Student_Image.objects.all()
    serializer_class = StudentImage



# @csrf_exempt
# def StudentViewSet(request):
#     if request.method == "POST":
#         student_admission_status = request.POST.get('student_admission_status')
#         student_name = request.POST.get('student_name')
#         student_DOB = request.POST.get('student_DOB')
#         student_father = request.POST.get('student_father')
#         student_mother = request.POST.get('student_mother')
#         student_category = request.POST.get('student_category')
#         student_gender = request.POST.get('student_gender')
#         student_nationality = request.POST.get('student_nationality')
#         student_domicile = request.POST.get('student_domicile')
#         student_blood = request.POST.get('student_blood')
#         student_email = request.POST.get('student_email')
#         student_parent_email = request.POST.get('student_parent_email')
#         student_ph = request.POST.get('student_ph')
#         student_father_ph = request.POST.get('student_father_ph')
#         student_aadhar = request.POST.get('student_aadhar')
#         student_corr_address1 = request.POST.get('student_corr_address1')
#         student_corr_address2 = request.POST.get('student_corr_address2')
#         student_corr_city = request.POST.get('student_corr_city')
#         student_corr_district = request.POST.get('student_corr_district')
#         student_corr_country = request.POST.get('student_corr_country')
#         student_corr_state = request.POST.get('student_corr_state')
#         student_corr_pincode = request.POST.get('student_corr_pincode')
#         student_parr_address1 = request.POST.get('student_parr_address')
#         student_parr_address2 = request.POST.get('student_parraddress')
#         student_parr_city = request.POST.get('student_parrcity')
#         student_parr_district = request.POST.get('student_parrdistrict')
#         student_parr_state = request.POST.get('student_parrstate')
#         student_parr_country = request.POST.get('student_parrcountry')
#         student_parr_pincode = request.POST.get('student_parrpincode')
#         student_course = request.POST.get('student_course')
#         # student_batch = request.POST.get('student_batch')
#         # student_fee_pattern = request.POST.get('student_fee')
#         # student_image = request.POST.get('student_')
#         print("abc")
#         free = database.child('StudentDetails').child('free').shallow().get().val()
#         print("hhh")
#         if free:
#             print("aaa")
#             tepid = free
#             print(tepid)
#         else:
#             print('ccc')
#             tepid = 1000000
#         print("xyz")
#         database.child('StudentDetails').child("S"+str(tepid)).child('details').update(
#             {
#                 'student_admission_status': student_admission_status,
#                 'student_name': student_name,
#                 'student_DOB': student_DOB,
#                 'student_father': student_father,
#                 'student_mother': student_mother,
#                 'student_catedory': student_category,
#                 'student_gender': student_gender,
#                 'student_nationality': student_nationality,
#                 'student_domicile': student_domicile,
#                 'student_blood': student_blood,
#                 'student_email': student_email,
#                 'student_parent_email': student_parent_email,
#                 'student_ph': student_ph,
#                 'student_father_ph': student_father_ph,
#                 'student_aadhar': student_aadhar,
#                 'student_corr_address1': student_corr_address1,
#                 'student_corr_address2': student_corr_address2,
#                 'student_corr_city': student_corr_city,
#                 'student_corr_district': student_corr_district,
#                 'student_corr_state': student_corr_state,
#                 'student_corr_country': student_corr_country,
#                 'student_corr_pincode': student_corr_pincode,
#                 'student_parr_address1': student_parr_address1,
#                 'student_parr_address2': student_parr_address2,
#                 'student_parr_city': student_parr_city,
#                 'student_parr_district': student_parr_district,
#                 'student_parr_state': student_parr_state,
#                 'student_parr_country': student_parr_country,
#                 'student_parr_pincode': student_parr_pincode,
#                 'student_course': student_course,
#                 'student_batch': "",
#                 'student_fee_pattern': "",
#             }
#         )
#         database.child('StudentDetails').update({'free':tepid+1})
#         return JsonResponse({'success':'student registered successfully and your registration id is R'+str(tepid)})
#     else:
#         student = database.child('StudentDetails').get()
#         l=[]
#         print(student.val())
#         if student.val():
#             for i in student:
#                 if i.key()!='free':
#                     print(i.val())
#                     l.append(
#                         {
#                             'id':i.key(),
#                             'student_admission_status': i.val()['details']['student_admission_status'],
#                             'student_name': i.val()['details']['student_name'],
#                             'student_DOB': i.val()['details']['student_DOB'],
#                             'student_father': i.val()['details']['student_father'],
#                             'student_mother': i.val()['details']['student_mother'],
#                             'student_catedory': i.val()['details']['student_category'],
#                             'student_gender': i.val()['details']['student_gender'],
#                             'student_nationality': i.val()['details']['student_nationality'],
#                             'student_domicile': i.val()['details']['student_domicile'],
#                             'student_blood': i.val()['details']['student_blood'],
#                             'student_email': i.val()['details']['student_email'],
#                             'student_parent_email': i.val()['details']['student_parent_email'],
#                             'student_ph': i.val()['details']['student_ph'],
#                             'student_father_ph': i.val()['details']['student_father_ph'],
#                             'student_aadhar': i.val()['details']['student_aadhar'],
#                             'student_corr_address1': i.val()['details']['student_corr_address1'],
#                             'student_corr_address2': i.val()['details']['student_corr_address2'],
#                             'student_corr_city': i.val()['details']['student_corr_city'],
#                             'student_corr_district': i.val()['details']['student_corr_district'],
#                             'student_corr_state': i.val()['details']['student_corr_state'],
#                             'student_corr_country': i.val()['details']['student_corr_country'],
#                             'student_corr_pincode': i.val()['details']['student_corr_pincode'],
#                             'student_parr_address': i.val()['details']['student_parr_address1'],
#                             'student_parraddress': i.val()['details']['student_parr_address2'],
#                             'student_parrcity': i.val()['details']['student_parr_city'],
#                             'student_parrdistrict': i.val()['details']['student_parr_district'],
#                             'student_parrstate': i.val()['details']['student_parr_state'],
#                             'student_parrcountry': i.val()['details']['student_parr_country'],
#                             'student_parrpincode': i.val()['details']['student_parr_pincode'],
#                             'student_course': i.val()['details']['student_course'],
#                             'student_batch': i.val()['details']['student_batch'],
#                             'student_fee_pattern': i.val()['details']['student_fee_pattern'],
#                         }
#                     )
#         return JsonResponse({'data': l})


        
        
        