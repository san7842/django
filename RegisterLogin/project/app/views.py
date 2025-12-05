from django.shortcuts import render

# Create your views here.
def landing(req):
    return render(req,'landing.html')
def register(req):
    return render(req,'register.html')
def registerdata(req):
    if req.method=='POST':
        n=req.POST.get('Name')
        e=req.POST.get('Email')
        c=req.POST.get('Contact')
        d=req.POST.get('Details')
        i=req.FILES.get('Image')
        print(n,e,c,d,i)
        user=Student.objects.filter(Email=e)
        if user:
            msg="Email already exist"
            return render(req,'register.html',{'msg':msg})
        else:
            Student.objects.Create(Name=n,Email=e,Contact=c,Details=d,Image=i)
            return(req,'register.html',{'msg':"data save"})