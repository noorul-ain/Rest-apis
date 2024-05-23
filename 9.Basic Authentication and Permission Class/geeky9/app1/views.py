
from rest_framework import viewsets
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated,AllowAny
from app1.serializers import StudentSerializer
from app1.models import Student


class StudentModelViewSet(viewsets.ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    authentication_classes = [BasicAuthentication]  # Specify the desired authentication class/es
    permission_classes = [IsAuthenticated]  # Add any desired permission classes
    parser_classes = [AllowAny]


    # All registerd user(admin and other) can easliy access data through username and password,,,IN case of  [IsAuthenticated]




