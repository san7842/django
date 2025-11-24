from django.shortcuts import render
# def myrender(req):
#     return render(req,'first.HTML')
def myrender(req):
    email="sandeepjjjj@gmail.com"
    name="sandeep"
    data={"n":name,"e":email}
    return render(req,'new.html',data)

# Create your views here.
def home(req):
    return render(req,'home.html')

def about(req):
    return render(req,'about.html')

def contact(req):
     return render(req,'contact.html')

def services(req):
    return render(req,'services.html')

def register(req):
     return render(req,'register.html')

def login(req):
    return render(req,'login.html')