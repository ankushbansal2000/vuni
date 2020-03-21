from .models import Student_Details
from rest_framework import generics,filters,response
from .serializer import StudentSerializers
class StudentViewSet(generics.ListCreateAPIView):
    serializer_class = StudentSerializers
    def get_queryset(self):
        if self.request.method == 'POST':
            queryset = Student_Details.objects.all()
        elif self.request.method == 'GET':
            queryset = Student_Details.objects.all()
            return queryset
        else:
            return response("please choose the right method")

class SearchStudent(generics.ListAPIView):
    queryset = Student_Details.objects.all()
    serializer_class = StudentSerializers
    filter_backends = [filters.SearchFilter]
    search_fields = ['student_name','id']