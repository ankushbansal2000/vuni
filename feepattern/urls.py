from django.urls import path
from .views import Fee
urlpatterns = [
    path('fee',Fee.as_view()),
]
