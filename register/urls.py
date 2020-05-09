from django.urls import path,include
from .views import StudentViewSet,SearchStudent,StudentRegistrationUpdate,ImageViewSet
from django.conf import settings
from django.conf.urls.static import static
from rest_framework import routers

router = routers.DefaultRouter()
router.register('put',StudentRegistrationUpdate)
router.register('image',ImageViewSet)


urlpatterns = [
    # path('api-auth/', include('rest_framework', namespace='rest_framework')),
    path('reg',StudentViewSet.as_view()),
    path(r'',SearchStudent.as_view()),
]
urlpatterns += router.urls
urlpatterns = urlpatterns + static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
