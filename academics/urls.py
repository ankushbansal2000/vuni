from django.urls import path
from .views import addBatch,seebatch

urlpatterns = [
    path('batch',addBatch.as_view()),
    path('getbatch',seebatch),
]
