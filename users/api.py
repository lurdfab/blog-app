from django.shortcuts import render
from rest_framework.generics import GenericAPIView
from .models import User
from .serializers import *
from rest_framework.response import Response
from rest_framework  import status, permissions
from rest_framework.request import Request
from django.contrib.auth import authenticate
from .tokens import create_jwt_pair_for_user


class RegisterView(GenericAPIView):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
   

    def post(self, request:Request):  
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save()
            response = {
                "message":"user created successfully",
                "data":serializer.data
            }

            return Response(data=response, status=status.HTTP_201_CREATED)

        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST )

   
class LoginView(GenericAPIView):
    serializer_class = LoginSerializer

    
    def post(self, request:Request): 
        username= request.data.get('username')
        password = request.data.get('password')

        user=authenticate(username=username, password=password)

        if user is not None:

            tokens = create_jwt_pair_for_user(user)
            response = {
                "message": "Login was succesful",
                "tokens": tokens
            }
            return Response(data=response, status=status.HTTP_200_OK)
        else:
            return Response(data={"message": "invalid username and password"})

    def get(self, request:Request): 
        content = {
            "user":str(request.user),
            "auth":str(request.auth)
        }
        return Response(data=content, status=status.HTTP_200_OK )
    
class LogoutView(GenericAPIView):
    # authentication_classes = [JWTAuthentication]  # Use the appropriate authentication method
  

    def post(self, request):
        # When a user logs out, you can simply delete their token (or perform other necessary actions).
        request.auth.delete()  # Delete the token
        return Response(status=status.HTTP_204_NO_CONTENT)