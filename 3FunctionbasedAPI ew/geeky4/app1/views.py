from django.shortcuts import render
from rest_framework.decorators import api_view
from django.http import HttpResponse
from rest_framework.response import Response
from .models import Student
from .serializers import StudentSerializer
from rest_framework import status

# Create your views here.

#----->>>>>>>>>Function Based API View in Django REST Framework 

@api_view(['GET','POST','PUT','DELETE','PATCH'])
def hello_world(request,pk=None):
    if request.method == 'GET':
        id =  pk
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        else:
            stu = Student.objects.all()
            serializer = StudentSerializer(stu, many=True)
            return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method =='PUT': #complete update
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':'Data update'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        id = request.data.get('id')
        stu = Student.objects.get(pk=id)
        stu.delete()
        return Response({'msg':'Data deleted'})
    
     
    if request.method =='PATCH': 
        id = pk
        stu = Student.objects.get(pk=id)
        serializer = StudentSerializer(stu=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response({'msg':' Partialy Data update'})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
            
