from django.shortcuts import render
from .models import User
from .serializers import UserSerializer
from rest_framework import viewsets
from rest_framework.authentication import SessionAuthentication
from .custompermission import MyPermission
# Create your views here.
#--->>>>Session Authentication and Permission
class StudentViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = (SessionAuthentication,)
    permission_classes = [MyPermission]
   



   

