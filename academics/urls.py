from django.urls import path
from .views import addBatch

urlpatterns = [
    path('batch',addBatch.as_view())
]
