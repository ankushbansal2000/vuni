from django.urls import path
from .views import addBatch,seebatch,excelByBatch

urlpatterns = [
    path('batch',addBatch.as_view()),
    path('getbatch',seebatch),
    path('excelByBatch',excelByBatch),
]
