from .models import Student_Details,Student_Image
from rest_framework import generics,filters,viewsets
from .serializer import StudentSerializers,StudentGet,StudentUpdate,StudentImage
from rest_framework.exceptions import MethodNotAllowed
# class StudentViewSet(generics.ListCreateAPIView):
#     def get_serializer_class(self):
#         if self.request.method == "POST":
#             serializer_class = StudentSerializers
#             return serializer_class
#         elif self.request.method == "GET":
#             serializer_class = StudentGet
#             return serializer_class
#         else:
#             raise MethodNotAllowed
#     def get_queryset(self):
#         if self.request.method == 'POST':
#             queryset = Student_Details.objects.all()
#             return queryset
#         elif self.request.method == 'GET':
#             queryset = Student_Details.objects.all()
#             return queryset
#         else:
#             raise MethodNotAllowed

class SearchStudent(generics.ListAPIView):
    queryset = Student_Details.objects.all()
    serializer_class = StudentSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['student_name','id']

class StudentRegistrationUpdate(viewsets.ModelViewSet):
    queryset = Student_Details.objects.all()
    serializer_class = StudentUpdate
    

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Student_Image.objects.all()
    serializer_class = StudentImage


def StudentViewSet(request):
    if request.method == "POST":
        AS = request.POST.get('student_admission_status')
        name = request.POST.get("student_name")
        DOB = request.POST.get("student_DOB")
        father = request.POST.get('student_father')
        mother = request.POST.get('student_mother')
        category = request.POST.get('student_category')
        gen = request.POST.get('student_gender')
        nation = request.POST.get('student_nationality')
        domicile = request.POST.get('student_domicile')
        blood = request.POST.get('student_blood')
        mail = request.POST.get('student_email')
        parent_email = request.POST.get('student_parent_email')
        ph = request.POST.get('student_ph')
        phno = request.POST.get('student_parent_ph')
        aadhar = request.POST.get("student_aadhar")
        corr_add1 = request.POST.get('student_corr_address1')
        corr_add2 = request.POST.get('student_corr_address2')
        corr_city = request.POST.get('student_corr_city')
        corr_dist = request.POST.get('student_corr_district')
        corr_state = request.POST.get('student_corr_state')
        corr_country = request.POST.get('student_corr_country')
        corr_pin = request.POST.get('student_corr_pincode')
        parr_add1 = request.POST.get('student_parr_address1')
        parr_add2 = request.POST.get('student_parr_address2')
        parr_city = request.POST.get('student_parr_city')
        parr_dist = request.POST.get('student_parr_district')
        parr_state = request.POST.get('student_parr_state')
        parr_country = request.POST.get('student_parr_country')
        parr_pin = request.POST.get('student_parr_pincode')
        course = request.POST.get('student_course')
        batch = request.POST.get('student_batch')
        year = request.POST.get('student_academic_year')
        category = request.POST.get('student_admission_category')
        fee_category = request.POST.get('student_fee_category')


        return (AS)
        
        
        