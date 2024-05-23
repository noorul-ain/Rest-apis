from django.shortcuts import render
from . serializers import StudentSerializer
from . models import Student
import io
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
# --->>>>>>>>>>>>>>Decerilizations---------
@csrf_exempt
def student_create(request):
    if request.method == 'POST':
        json_data = request.body #request body data put into the json_data
        stream = io.BytesIO(json_data) #json data convert ino stream
        pythondata = JSONParser().parse(stream) #strean into pythondata
        serializer = StudentSerializer(data = pythondata) # python data convert into complex
        if serializer.is_valid():
            serializer.save()
            response_data = {'msg':'Data Created'}
            json_data = JSONRenderer().render(response_data) 
            return HttpResponse(json_data, content_type='application/json')
    json_data = JSONRenderer().render(serializer.errors)
    return HttpResponse(json_data, content_type='application/json')





