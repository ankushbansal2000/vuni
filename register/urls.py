from django.urls import path,include
from .views import StudentViewSet,SearchStudent,StudentRegistrationUpdate
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

router = routers.DefaultRouter()
router.register('put',StudentRegistrationUpdate)


urlpatterns = [
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('reg',StudentViewSet.as_view()),
    path(r'',SearchStudent.as_view()),
    # path('get/',router.urls),
]
urlpatterns += router.urls