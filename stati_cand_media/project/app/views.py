from django.shortcuts import render

# Create your views here.
def landing(req):
    return render(req,'landing.html')
def dashboard(req):
    data=Student.objects.all()
    return render(req,'dashboard.html')