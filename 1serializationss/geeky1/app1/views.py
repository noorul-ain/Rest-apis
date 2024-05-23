from django.shortcuts import render
from .models import Student
from .serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
# Create your views here.

#->>>>>>>>>>>>>>>>Serializer and Serializertion in Django REST Framework

# -->>>>>>>Model Object Single User 
def student_details(request,pk):
    stu = Student.objects.get(id = pk)#that is complex data
    # print(stu)
    serializer = StudentSerializer(stu)#to convert python native
    # print(serializer)
    json_data = JSONRenderer().render(serializer.data)#to convert jsondata
    # print(json_data)
    return HttpResponse(json_data, content_type='application/json')#sent to the client as a response
    # return JsonResponse(serializer.data)

# ---->>>>>>>>>>>>Multiple user
def student_list(request):
    stu = Student.objects.all()#that is complex data
    # print(stu)
    serializer = StudentSerializer(stu,many=True)#to convert python native
    # print(serializer)
    json_data = JSONRenderer().render(serializer.data)#to convert jsondata
    # print(json_data)
    return HttpResponse(json_data, content_type='application/json')#sent to the client as a response
    # return JsonResponse(serializer.data, safe=False)
