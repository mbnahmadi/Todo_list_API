# from django.shortcuts import render
from .serializer import registerUserSerializer
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework import generics
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.tokens import RefreshToken 
# # from
# # Create your views here.

User = get_user_model()

class RegisterUserView(APIView):
    @swagger_auto_schema(request_body=registerUserSerializer)

    def post(self,request):
        serializer = registerUserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()

            refresh = RefreshToken.for_user(user)
            access = str(refresh.access_token)
            return Response({
                            'user':{
                                'name':user.name , 
                                'email':user.email
                                } ,
                            'token':{
                                'refresh': str(refresh),
                                'access_token':str(access)
                                }
                            },
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    
    


# class LoginUserView(APIView):
    


