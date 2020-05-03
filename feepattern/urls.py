from django.urls import path
from .views import Fee,FeeHead
urlpatterns = [
    path('fee',Fee.as_view()),
    path('feehead',FeeHead.as_view())
]
