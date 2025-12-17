from django.shortcuts import render

# Create your views here.
def login_data(req):
    if req.method=='POST':
        e=req.GET.get()
    
