from django.urls import path
from .views import Fee,FeeHead,seefee,studentsFeeDetails,feePay
urlpatterns = [
    path('fee',Fee.as_view()),
    path('feehead',FeeHead.as_view()),
    path('getfee',seefee),
    path('studentsFeeDetails',studentsFeeDetails),
    path('feepay',feePay),
]
