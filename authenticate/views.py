from django.shortcuts import render
from .serializer import registerSerializer
from .models import User
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from drf_yasg.utils import swagger_auto_schema
# from
# Create your views here.


class registerView(APIView):
    @swagger_auto_schema(request_body=registerSerializer)

    def post(self,request):
        serializer = registerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            
            return Response({'message':'User create successfuly!'} , status=status.HTTP_201_CREATED)
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)    