from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from .models import Student
from.serializers import StudentSerializer
from rest_framework.views import APIView

# Create your views here.
class StudentList(APIView):
    def get(self, request, pk=None, format=None):
        id = pk 
        if id is not None:
            stu = Student.objects.get(id=id)
            serializer = StudentSerializer(stu)
            return Response(serializer.data)
        
        stu = Student.objects.all()
        serializer = StudentSerializer(stu, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def put(self , request,pk, formate=None):
        id = pk
        stu = Student.objects.get(id=pk)
        serializer = StudentSerializer(stu,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def Patch(self, request,pk, formate=None):
        id = pk
        stu = Student.objects.get(id=pk)
        serializer = StudentSerializer(stu,data=request.data,parial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete(self, request, pk=None, format=None):
        id = pk
        stu = Student.objects.get(id=pk)
        stu.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
            