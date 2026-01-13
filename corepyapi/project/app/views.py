from django.shortcuts import render
from .models import Movies
from django.http import HttpResponse
from django.forms import model_to_dict
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
@csrf_exempt   
def movies_details(req,pk):
    if req.method=='PUT':
    
        j_data=req.body
        # print(j_data)
        # print(type(j_data))
        n_data=json.loads(j_data)
        # print(n_data)
        # print(type(n_data))
        o_data=Movies.objects.get(id=pk)
        # po_data=model_to_dict(o_data)
        # po_data['name']=n_data['name']
        # po_data['dis']=n_data['dis']
        # po_data['action']=n_data['action']
        if (n_data.get('name',False) and n_data.get('dis',False) and n_data('active',False)):
            o_data.name=n_data['name']
            o_data.dis=n_data['dis']
            o_data.active=n_data['active']
            o_data.save()
        
            d={'msg':"objects update successfully"}
            jd=json.dumps(d)
            return HttpResponse(jd,content_type='applications/json')
        else:
              d={'msg':"objects not found"}
              jd=json.dumps(d)
              return HttpResponse(jd,content_type='applications/json')
    # elif req.method=='PATCH':
    #     pass
    # elif req.method=='DELETE':
    #     pass
    # data=Movies.objects.get(id=pk)
    # print(data)
    # print(type(data))
    # p_data=model_to_dict(data)
    # print(p_data)
    # print(type(p_data))
    # j_data=json.dumps(p_data)
    # return HttpResponse(j_data,content_type='application/json')
    if req.method=='PATCH':
        
        j_data=req.body
        # print(j_data)
        # print(type(j_data))
        n_data=json.loads(j_data)
        # print(n_data)
        # print(type(n_data))
        o_data=Movies.objects.get(id=pk)
        # po_data=model_to_dict(o_data)
        # po_data['name']=n_data['name']
        # po_data['dis']=n_data['dis']
        # po_data['action']=n_data['action']

        # if (n_data.get('name',False) and n_data.get('dis',False) and n_data('active',False)):
        #     o_data.name=n_data['name']
        #     o_data.dis=n_data['dis']
        #     o_data.active=n_data['active']
        #     o_data.save()
        if n_data.get('name',False):
            o_data.name=n_data['name']
        if n_data.get('dis',False):
            o_data.dis=n_data['dis']
        if n_data.get('active',False):
            o_data.active=n_data['active']
        o_data.save()
        
        d={'msg':"objects partially  update successfully"}
        jd=json.dumps(d)
        return HttpResponse(jd,content_type='applications/json')
        # else:
        #       d={'msg':"objects not found"}
        #       jd=json.dumps(d)
        #       return HttpResponse(jd,content_type='applications/json')
    if req.method=='DELETE':
        id=Movies.objects.filter(id=pk)
        if id:

            data=Movies.objects.get(id=pk)
            data.delete()
            p_data={'msg':"object delete"}
            j_data=json.dumps(p_data)
            return HttpResponse(j_data,content_type='application/json')
        p_data={'msg':"id not present in db"}
        j_data=json.dumps(p_data)
        return HttpResponse(j_data,content_type='application/json')
    
            