from django.shortcuts import render,redirect
from .models import Aadhar,Student

# Create your views here.
def landing(req):
    return render(req,'landing.html')
def add_aadhar(req):
    if req.method=='POST':
        aadharno=req.POST.get('aadharno')
        createDate=req.POST.get('createdate')
        createBy=req.POST.get('createby')
        Aadhar.objects.create(
         
         Aadhar_no=Aadharno,
         Create_date=
        )
        return redirect()
    return redirect(req,'add_aadhar')
def add_student(req):
    all_aadhar=Aadhar.objects.all()
    return render(req,'add_student.html',{'data':all_aadhar})

def show_aadhar(req):
    return render(req,'show_aadhar.html')

def show_student(req):
    studentdata=Student.objects.all().order_by()
    return render(req,'show_student.html',{'studentdata':studentdata})
def relation(req):
    # relation=Student.objects.all()
    # for i in relation:
    #     print(i. stu_name)
    #     print(i. stu_email)
    #     print(i. stu_contact)
    #     print(i. stu_aadhar.Aadharno)
    #     print(i. stu_aadhar.Created_by)
    #     print(i. stu_aadhar.Created_date)

    # through reverse access
    all_data=Aadhar.objects.all()
    for i in all_data:
        print(i.Aadharno)
        print(i.Created_by)
        print(i.Created_date)
        print(i.Student.stu_name)
        print(i.student.stu_email)
        print(i.student.stu_contact)
        

