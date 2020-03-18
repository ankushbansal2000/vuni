from django.shortcuts import render
from .models import Student_Details
from django.http import HttpResponse
# Create your views here.
def student_register(request):
    return render(request, "registration.component.html")

def student_save(request):
    stu=Student_Details.objects.all()
    return HttpResponse(stu)