from django.urls import path,include
from .views import StudentViewSet,SearchStudent
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('reg',StudentViewSet.as_view()),
    path(r'',SearchStudent.as_view()),
]