from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from .serializers import Student1
from rest_framework.renderers import JSONRenderer
from django.views.decorators.csrf import csrf_exempt
import io
from rest_framework.parsers import JSONParser

# Create your views here.
@csrf_exempt
def stu_list(req):
    if req.method=='POST':
        j_data = req.body
        print(j_data)
        print(type(j_data))
        stream = io.BytesIO(j_data)
        print(stream)
        print(type(stream))
        p_data = JSONParser().parse(stream)
        print(p_data)
        print(type(p_data))
        serializer=Student1(data=p_data)
        print(serializer)
        print(type(serializer))
        if serializer.is_valid():
            serializer.save()
            return HttpResponse({'msg':'data save'})
    # data=Student.objects.all()
    # serializer=Student1(data,many=True)
    # print(serializer)
    # print(serializer.data)
    # json = JSONRenderer().render(serializer.data)
    # print(json)
    # print(type(json))
    # return HttpResponse(json,content_type='application/json')
def stu_details(req ,pk):
    data=Student.objects.get(id=pk)
    serializer=Student1(data)
    print(serializer)
    print(serializer.data)
    json = JSONRenderer().render(serializer.data)
    print(json)
    print(type(json))
    return HttpResponse(json,content_type='application/json')
