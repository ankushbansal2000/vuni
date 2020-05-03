from django.urls import path
from .views import addBatch

urlpatterns = [
    path('',addBatch.as_view())
]
