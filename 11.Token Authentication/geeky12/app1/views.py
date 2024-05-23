from django.shortcuts import render
from .models import student
from .serializers import StudentSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from rest_framework.views import obtain_auth_token
# Create your views here.

#---->>>>>>>Token Authentication

class StudentViewSet(viewsets.ModelViewSet):
    queryset = student.objects.all()
    serializer_class = StudentSerializer
    # authentication_classes = (TokenAuthentication,)
    # permission_classes = (IsAuthenticated,)