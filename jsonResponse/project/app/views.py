from django.shortcuts import render
from django.http import JsonResponse
# def landing(req):
#     data={"name":"sandeep",
#           "age":24,
#           "quali":"b.tech"}
#     return JsonResponse(data)

def landing(req):
    # data=[1,2,3,4,5,'python']
    #data=(1,2,3,4,5,'python')
    #data='python'
    #data={1,2,3.4,5,'python'}
    data=10
    return JsonResponse(data,safe=False)
# Create your views here.
