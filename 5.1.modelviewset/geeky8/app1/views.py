
from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework import viewsets  # Note the plural 's' in viewsets


# Create your views here.
class StudentModelViewSet(viewsets.ModelViewSet):  # Corrected the typo: 'viewset' to 'viewsets'
    queryset = Student.objects.all()
    serializer_class = StudentSerializer

# 

class StudentReadOnlyModelViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer