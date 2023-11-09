from rest_framework import serializers
from .models import *
from rest_framework.validators import ValidationError
from rest_framework.authtoken.models import Token

class RegisterSerializer(serializers.ModelSerializer):
    #reason we do these below even after listing the fields in the class meta is to enforce certain parameters for the fields, we can do without it 
    email = serializers.CharField(max_length=100)
    username = serializers.CharField(max_length=20, min_length=5)
    password = serializers.CharField(max_length=128, min_length=8, write_only=True) #we used write only because we don't want it returned back to the server

    class Meta:
        model = User
        fields = ('username', 'email', 'first_name', 'last_name', 'password')

    def validate(self, attrs): #this method is used to validate our emails to avoid an email being used twice

        email_exists = User.objects.filter(email=attrs["email"]).first()
        if email_exists:
            raise ValidationError("Email already exists")
        return super().validate(attrs)
        
    def create(self, validated_data): #this method is used to hash password & generate token during registration.
        password = validated_data.pop("password")
        user = super().create(validated_data)
        user.set_password(password)
        user.save()
        Token.objects.create(user=user)
        return user
    

class LoginSerializer(serializers.ModelSerializer):
    #reason we do these below even after listing the fields in the class meta is to enforce certain parameters for the fields, we can do with it 

    username = serializers.CharField(max_length=20, min_length=5)
    password = serializers.CharField(max_length=128, min_length=8, write_only=True) #we used write only because we don't want it returned back to the server

    class Meta:
        model = User
        fields = ('username', 'password')