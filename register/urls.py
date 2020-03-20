from django.urls import path,include
from .views import StudentViewSet
from django.conf import settings
from django.conf.urls.static import static
# from rest_framework import routers



urlpatterns = [
    # path(r'',include(routers.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('reg',StudentViewSet.as_view())

]