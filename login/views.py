from rest_framework import generics
from rest_framework.response import Response
from rest_framework.exceptions import NotFound,ValidationError
from rest_framework_simplejwt.tokens import RefreshToken
import rest_framework_simplejwt
import jwt
from . import serializers,models
# Create your views here.

class UserRegistration(generics.CreateAPIView):
    def get_serializer_class(self):
        if self.request.method == "POST":
            return serializers.UserRegisterSerializer
    def post(self, request, *args, **kwargs):               #save user
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        response = Response({
            "success": "user has been successfully register",
        })
        return response



class UserLogin(generics.GenericAPIView):
    def get_tokens_for_user(self, user):
        refresh = RefreshToken.for_user(user)

        return {
                'refresh': str(refresh),
                'access': str(refresh.access_token),
                }
    serializer_class = serializers.UserLoginSerializer
    def post(self, request, *args, **kwargs):

        if not request.data:
            return Response({"Error": "Please provide username/password"}, status="400")
        username = request.data['username']
        password = request.data['password']
        print(username,password)
        try:
            user = models.UserDetails.objects.get(username=username, password=password)
        except:
            return Response({"Error": "Invalid username/password"}, status="400")
        if user:
            jwt_token = self.get_tokens_for_user(user)
            payload = jwt.decode(jwt_token['access'], 'SECRET_KEY')
            print(payload)
            print(payload['username'])

            return Response({
                "access" : jwt_token,
                'payload' : payload
                }
            )
        else:
            print("124")
            return Response(
              {'Error': "Invalid credentials"},
              status=400,
              content_type="application/json"
            )

