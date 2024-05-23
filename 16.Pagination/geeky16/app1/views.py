from rest_framework.generics import ListAPIView
from .models import Student
from .serializers import StudentSerializer

from .mypagungg  import MyPageNumber


class StudentList(ListAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = MyPageNumber


