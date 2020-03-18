from django.urls import path
from .views import student_register,student_save
urlpatterns = [
    path("reg",student_register),
    path("student",student_save),
]
