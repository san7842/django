from django.shortcuts import render
from .models import Movies
from django.http import HttpResponse
import json
from django.views.decorators.csrf import csrf_exempt

# Create your views here.
@csrf_exempt
def movies_list(req):
    # if req.method=='POST':
    #     j_data=req.body
    #     print(j_data)
    if req.method=='POST':
        data=req.body
        print(data)
        p_data=json.loads(data)
        print(p_data)
        print(type(p_data))
        for i in p_data:
        #   n=i['name']
        #   d=i['dis']
        #   a=i.get('active',True)
          Movies.objects.create(name=i['name'],dis=i['dis'],active=i['active'])
        # Movies.objects.create(name=p_data['name'],dis=p_data['dis'],active=p_data['active'])
        d={'msg':"object create successfully"}
        i_d=json.dumps(d)
        return HttpResponse(i_d,content_type="application/json")
    else:


        data=Movies.objects.all()
        # print(data)
        # print(data.values())
        # print(list(data.values()))
        data=list(data.values())
        j_data=json.dumps(data)
        print(j_data)
        return HttpResponse(j_data,content_type='application/json')