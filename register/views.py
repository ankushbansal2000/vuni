from .models import Student_Details,Student_Image
from rest_framework import generics,filters,viewsets
from .serializer import StudentSerializers,StudentGet,StudentUpdate,StudentImage
from rest_framework.exceptions import MethodNotAllowed
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

class StudentRegistrationUpdate(viewsets.ModelViewSet):
    queryset = Student_Details.objects.all()
    serializer_class = StudentUpdate
    

class ImageViewSet(viewsets.ModelViewSet):
    queryset = Student_Image.objects.all()
    serializeer_class = StudentImage
