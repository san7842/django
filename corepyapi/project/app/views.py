from django.shortcuts import render
from .models import Movies
from django.http import HttpResponse
import json

# Create your views here.
def movies_list(req):
    if req.method=='POST':
        j_data=req.body
        print(j_data)


    data=Movies.objects.all()
    # print(data)
    # print(data.values())
    # print(list(data.values()))
    data=list(data.values())
    j_data=json.dumps(data)
    print(j_data)
    return HttpResponse(j_data,content_type='application/json')