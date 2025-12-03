from django.shortcuts import render
from .models import Student

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
     Student.objects.create(name=n,email=e,contact=c,details=d,image=i)
    #  data=Student.objects.all()
    #  return render(req,'data.html',{'key':data})
def stu_data(req):
    #  data=Student.objects.filter(name='Mr. Sandeep Sahu',email='sandeep@gmail.com')
    #  print(data)
    #  data=Student.objects.exclude(name='Mr. Sandeep Sahu')
    #  data=Student.objects.order_by('name')
    #  data=Student.objects.order_by('-name')
    #  data=Student.objects.order_by('-name')
    #  data=datas.reverse()
    #  data=Student.objects.all()[:5]
     data=(((Student.objects.all()).reverse()[:5])).reverse()
     return render(req,'data.html',{'key':data})