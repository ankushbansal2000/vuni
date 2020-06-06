from django.urls import path,include
from . import views
urlpatterns = [
    path('register',views.UserRegistration.as_view()),
    path('login',views.UserLogin.as_view())
]
