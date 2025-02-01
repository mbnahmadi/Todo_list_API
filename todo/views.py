from django.shortcuts import render, get_object_or_404
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.permissions import IsAuthenticated
from .models import TodoModel
from .serializer import TodoSerializer,getTodoSerializer
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from django.core.paginator import Paginator
# Create your views here.


class CreateTodoView(APIView):
    permission_classes=[IsAuthenticated]

    @swagger_auto_schema(
            request_body=TodoSerializer,
            manual_parameters=
            [
                openapi.Parameter('Authorization', openapi.IN_HEADER, description="Token", type=openapi.TYPE_STRING)
            ]
        )
    
    def post(self,request):
        serializer = TodoSerializer(data=request.data)
        if serializer.is_valid():
            save_todo = serializer.save(user=request.user)
            return Response({
                'message':'Todo create successfuly',
                'detail':{
                    'id':save_todo.pk
                    ,'title':save_todo.title,
                    'description':save_todo.description
                    }
                }
                ,status=status.HTTP_201_CREATED)
        return Response(status=status.HTTP_400_BAD_REQUEST)

class UpdateTodoView(APIView):
    permission_classes=[IsAuthenticated]

    @swagger_auto_schema(request_body=TodoSerializer,
                        manual_parameters=[openapi.Parameter('Authorization', openapi.IN_HEADER, description="Token", type=openapi.TYPE_STRING)])
    def put(self, request,pk):
        try:
            todo = TodoModel.objects.get(pk=pk)
        except TodoModel.DoesNotExist:
            return Response({'error': 'Todo not found.'}, status=status.HTTP_404_NOT_FOUND)
        # todo = get_object_or_404(TodoModel, pk=pk) instead of 4 line above

        if todo.user != request.user:
            return Response({'error': 'Forbidden'}, status=status.HTTP_403_FORBIDDEN)
        # self.check_object_permissions(request, todo) instead of 2 lines above

        serializer = TodoSerializer(data=request.data , instance=todo)
        if serializer.is_valid():
            save_todo = serializer.save()
            return Response({'message':'Todo update successfuly',
            'detail':{
                'id':save_todo.pk,
                'title':save_todo.title,
                'description':save_todo.description
                }
            })
        return Response(status=status.HTTP_400_BAD_REQUEST)


class DeleteTdoView(APIView):
    permission_classes=[IsAuthenticated]

    @swagger_auto_schema(request_body=TodoSerializer,
                        manual_parameters=[openapi.Parameter('Authorization', openapi.IN_HEADER, description="Token", type=openapi.TYPE_STRING)])
    def delete(self, request,pk):
        try:
            todo = TodoModel.objects.get(pk=pk)
        except:
            return Response({'error':'Todo not found'},status=status.HTTP_404_NOT_FOUND)
        if todo.user != request.user:
            return Response({"Forbidden"},status=status.HTTP_403_FORBIDDEN)  

        todo.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  

class GetTodoView(APIView):
    permission_classes=[IsAuthenticated]

    @swagger_auto_schema(manual_parameters=[
        openapi.Parameter('Authorization', openapi.IN_HEADER, description="Token", type=openapi.TYPE_STRING),
        openapi.Parameter('page', openapi.IN_QUERY, description="Page number", type=openapi.TYPE_INTEGER),
        openapi.Parameter('limit', openapi.IN_QUERY, description="Number of records per page", type=openapi.TYPE_INTEGER)
                                            ])
    
    def get(self,request):
        page = int(request.query_params.get('page'))
        limit = int(request.query_params.get('limit'))

        todos = TodoModel.objects.filter(user=request.user)
        paginator = Paginator(todos,limit)
        try:
            paginations = paginator.page(page)
        except:
            return Response({'error':'page not found'},status=status.HTTP_404_NOT_FOUND)    


        serializer = getTodoSerializer(paginations , many=True)
        return Response({
            'data':serializer.data,
            'page':paginator.num_pages ,
            'limit':limit , 
            'total':paginator.count
        })