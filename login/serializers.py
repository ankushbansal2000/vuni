from rest_framework import serializers
from . import models
#Register Api
class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserDetails
        fields = ['username','email','password']
        extra_kwargs = {'password':{'write_only':True}}


#Login Api
class UserLoginSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserDetails
        fields = ['username','password']

class UserShowSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserDetails
        fields = ['username','email','category']
