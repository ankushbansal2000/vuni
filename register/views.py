from .models import Student_Details
from rest_framework import viewsets,generics,filters
from .serializer import StudentSerializers
from rest_framework.decorators import api_view
# Create your views here.

# @api_view(['POST'])
class StudentViewSet(generics.ListAPIView,generics.CreateAPIView):
    serializer_class = StudentSerializers
    def get_queryset(self):
        if self.request.method == 'POST':
            queryset = Student_Details.objects.all()
        elif self.request.method == 'GET':
            queryset = Student_Details.objects.all()
            try:
                id = self.request.query_params.get('id')
                if id:
                    return queryset.filter(id=id)
                else:
                    stu_name = self.request.query_params.get('name')
                    return queryset.filter(student_name=stu_name)
            except:
                return queryset