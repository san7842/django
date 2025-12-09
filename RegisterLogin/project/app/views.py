from django.shortcuts import render,redirect
from .models import Student
from django.urls import reverse
from urllib.parse import urlencode
# Create your views here.
def landing(req):
    return render(req,'landing.html')
def register(req):
    return render(req,'register.html')
def registerdata(req):
    print(req.POST)
    if req.method=='POST':
        n=req.POST.get('Name')
        e=req.POST.get('Email')
        c=req.POST.get('Contact')
        d=req.POST.get('Details')
        i=req.FILES.get('Image')
        p=req.POST.get('Password')
        cp=req.POST.get('Cpassword')
        print(n,e,c,d,i)
        user=Student.objects.filter(Email=e)
        if user:
            msg="Already Exist"
            return render(req,'register.html',{'msg':msg})
        else:
            if p==cp:
                Student.objects.create(Name=n,Email=e,Contact=c,Details=d,Password=p)
                msg = "Registration Done"
                return render(req,'login.html',{'msg':msg})
            else:
                msg='p & cp not match'
                return render(req,'register.html',{'msg':msg})

def login(req):
    return render(req,'login.html')

def logindata(req):
    if req.method=='POST':
        #print(req.POST)
        e=req.POST.get('email')
        p=req.POST.get('password')
        #print(e,p)
        user=Student.objects.filter(Email=e)  
        if user:
            userdata=Student.objects.get(Email=e)
            un=userdata.Name
            ue=userdata.Email
            uc=userdata.Contact
            ud=userdata.Details
            ui=userdata.Image
            up=userdata.Password
            if up==p:
                data={'name':un,'email':ue,'contact':uc,'details':ud,'image':ui,'password':up}
                # return render(req,'dashboard.html',{'data':data})
                base_url=reverse('dashboard')
                data=urlencode({'name':un,'email':ue,'contact':uc,'details':ud,'image':ui,'password':up})
                return redirect(f'{base_url}?{data}')
            else:
                msg="Email @Password not match"
                return render(req,'login.html',{'msg':msg})
            
        else:
            msg="Email not register "
            return render(req,'register.html',{'msg':msg})
        # if user:
        #     msg="Email already exist"
        #     return render(req,'register.html',{'msg':msg})
        # else:
        #     Student.objects.Create(Name=n,Email=e,Contact=c,Details=d,Image=i)
        #     return(req,'register.html',{'msg':"data save"})
def dashboard(req):
            n=req.GET.get('name')
            e=req.GET.get('email')
            c=req.GET.get('contact')
            d=req.GET.get('details')
            i=req.GET.get('image')
            p=req.GET.get('password')

            # value=req.GET.get('data')
            # print(value)
            # e=value.get('email')
            # p=value.get('password')
            user=Student.objects.filter(Email=e)
            if user:
                 userdata=Student.objects.get(Email=e)
                 if p==userdata.password:
                      data=('name'=n,'email'=e,'contact'=c,'detail'=d,'image'=i,'password'=p)
                      return render(req,'dashboard.html',{'data':data})
                 else:
                      return redirect('login')
                 
            else:
                 return redirect('login')

