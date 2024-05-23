from django.shortcuts import render
from . models import Student
from . serializers import StudentSerializer
import io
from rest_framework.parsers import JSONParser
from . serializers import StudentSerializer
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse,JsonResponse
from django.views.decorators.csrf import csrf_exempt
from django.utils.decorators import method_decorator
from django.views import View

# Create your views here.

@method_decorator(csrf_exempt, name='dispatch')
# ----->>>get and read
class StudentAPI(View):
    def get(self, request, **kwargs):
            json_data = request.body 
            stream = io.BytesIO(json_data)
            pythondata = JSONParser().parse(stream)
            id = pythondata.get('id', None)
            if id is not None :
                stu = Student.objects.get(id=id)
                serializer = StudentSerializer(stu)
                json_data = JSONRenderer().render(serializer.data)
                return HttpResponse(json_data, content_type='application/json')
            stu = StudentSerializer(stu, many=True)
            serializer = StudentSerializer(stu)
            json_data = JSONRenderer().render(serializer.errors)
            return HttpResponse(json_data, content_type='application/json')
    # ----->>>>post used for create

    def post (self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        serializer = StudentSerializer(data=pythondata)
        if serializer.is_valid():
            serializer.save()  
            res = {'msg' 'Data Created'}    
            json_data = JSONParser().renderer(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONParser().renderer(res)
        return HttpResponse(json_data, content_type='application/json')
    # ----->>>put---update fot put method
    def put(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        #---Complete Update --Required ALL Data from Frontend/Client
        # serializer = StudentSerializer(stu,pythondata)
        #--Partial Update --Required ALL Data from
        serializer = StudentSerializer(stu,pythondata,partial =True)
        if serializer.is_valid():
            serializer.save()  
            res = {'msg' 'Data Updated'}    
            json_data = JSONParser().renderer(res)
            return HttpResponse(json_data, content_type='application/json')
        json_data = JSONParser().renderer(res)
        return HttpResponse(json_data, content_type='application/json')

       
#    ------>>>>>delete
    def delete(self, request, *args, **kwargs):
        json_data = request.body
        stream = io.BytesIO(json_data)
        pythondata = JSONParser().parse(stream)
        id = pythondata.get('id')
        stu = Student.objects.get(id=id)
        stu.delete()
        res = {'msg' 'Data Deleted'}    
        # json_data = JSONParser().renderer(res)
        # return HttpResponse(json_data, content_type='application/json')
        return JsonResponse(res,safe=False)
        
