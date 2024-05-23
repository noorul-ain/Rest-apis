from django.shortcuts import render
from . models import User
from . serializers import UserSerializer
from rest_framework.generics import ListAPIView,CreateAPIView,RetrieveAPIView,UpdateAPIView,DestroyAPIView
from rest_framework.generics import ListCreateAPIView,RetrieveUpdateAPIView,RetrieveDestroyAPIView,RetrieveUpdateDestroyAPIView

#  Create your views here.
    # get
class UserList(ListAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # post request
class UserCreate(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # 
class UserRetrieve(RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # put and Patch
class UserUpdate(UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    # dell
class UserDelete(DestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

# combination 🔥 List & Craete
class UserListCreate(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetriveUpdate(RetrieveUpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetriveDestroy(RetrieveDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class UserRetriveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
# combination 🔥 List & Craete
class UserListCreate(ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
class UserRetriveUpdateDestroy(RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer


