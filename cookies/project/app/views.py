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
        response.set_cookie('Name',n,max_age=60*5)
        response.set_cookie('Email',e)
        response.set_cookie('password',p)
       
        return response
def get_data(req):
   # print(req.COOKIES)
   n=req.COOKIES.get('Name')
   e=req.COOKIES.get('Email')
   p=req.COOKIES.get('password')
   data={'name':n,
         'email':e,
         'password':p}
   return render(req,'landing.html',{'data':data})
def delete_data(req):
    if req.COOKIES:
        response=render(req,'landing.html',{'msg':'cookies data delete'})
        response.delete_cookie('name')
        response.delete_cookie('email')
        if req.COOKIES.get('password'):
            return response
    else:
        msg='dont have cookies'
        return render(req,'landing.html',{'msg':msg})

