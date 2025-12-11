from django.shortcuts import render

# Create your views here.
def landing(req):
    return render(req,'landing.html')
def set1(req):
    return render(req,'landing.html',{'set1':'set1'})
def set_data(req):
    if req.method=='POST':
        n=req.POST.get('Name')
        e=req.POST.get('Email')
        p=req.POST.get('password')
        print(n,e,p)
        response=render(req,'landing.html',{'msg':'cookies set succesfull'})
        response.set_cookie('Name',n)
        response.set_cookie('Email',e)
        response.set_cookie('password',p)
        return response

