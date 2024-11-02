"""
URL configuration for config project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from .views import create_Todo,update_Todo,delete_Todo,get_Todo

urlpatterns = [
    path('create/', create_Todo.as_view() , name='create_Todo'),
    path('update/<str:pk>', update_Todo.as_view() , name='update_Todo'),
    path('delete/<str:pk>', delete_Todo.as_view() , name='delete_Todo'),
    path('get/', get_Todo.as_view() , name='get_Todo'),

]
# Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI5OTQyNzgwLCJpYXQiOjE3Mjk5MzkxODAsImp0aSI6ImYxNGEwMGZhZTdhYTQ3ZjNhN2QzMDA2MmUwN2Y4YTQyIiwidXNlcl9pZCI6Mn0.fT1NJzZ66B9bCnVpkUW1hXvsFA2ktuX1kxwweuE8H_I
# Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNzI5OTQ2MDgxLCJpYXQiOjE3Mjk5NDI0ODEsImp0aSI6IjJjZmE0ZWU0MDIxODRjYzE4NDU1NmY5OTRhYTU1NzA5IiwidXNlcl9pZCI6M30.ZVwayPMNUQh4WGQbhRtzCLtOLoIOSY9oiu0ClDACPdE