from django.shortcuts import render
from .forms import Registerform
# Create your views here.
def landing(req):
    return render(req,'landing.html')

def register(req):
    form=Registerform()
    return render(req,'register.html',{'fm':form})
def registerdata(req):
    if req.method=='POST':
        form=Registerform(req.POST,req.FILES)
        print(form)
        if form.is_valid():
             form.save()




