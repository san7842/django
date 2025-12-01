from django.shortcuts import render

# Create your views here.
def landing(req):
    return render(req,'landing.html')

def register(req):
    return render(req,'register.html')

def registerdata(req):
     print(req.method)
     print(req.POST)
     print(req.GET)
     print(req.FILES)
     n=req.POST.get('name')
     e=req.POST.get('email')
     c=req.POST.get('contact')
     d=req.POST.get('details')
     i=req.FILES.get('image')
     print(n,e,c,d,i)