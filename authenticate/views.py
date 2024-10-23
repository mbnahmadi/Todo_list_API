from django.shortcuts import render
from .serializer import registerSerializer
from .models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
from rest_framework_simplejwt.tokens import RefreshToken 
# from
# Create your views here.


class registerView(APIView):
    @swagger_auto_schema(request_body=registerSerializer)

    def post(self,request):
        serializer = registerSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response({'message':'User create successfuly!',
                            'user':{'name':user.name , 'email':user.email} ,
                            'refresh':str(refresh),'access_token':str(refresh.access_token)} ,
                            status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    