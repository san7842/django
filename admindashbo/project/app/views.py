from django.shortcuts import render

# Create your views here.
# def login_data(req):
#     if req.method=='POST':
#         e=req.GET.get()
def adminpanel(req):
    return render(req,'adminpanel.html')
def login(req):
    return render(req,'login.html')
def login_data(req):
    return render(req,'login_data.html')
def forget(req):
    return render(req,'forget.html')
def employee_list(req):
    return render(req,'forget.html')
    

