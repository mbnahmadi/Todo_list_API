from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import TodoModel
from .serializer import TodoSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi

# Create your views here.


class create_Todo(APIView):
    permission_classes=[IsAuthenticated]

    @swagger_auto_schema(request_body=TodoSerializer,
                        manual_parameters=[openapi.Parameter('Authorization', openapi.IN_HEADER, description="JWT Token", type=openapi.TYPE_STRING)])
    
    def post(self,request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({'message':'Todo create successfuly'} , status=status.HTTP_201_CREATED)

