from django.shortcuts import render,redirect
from .models import Employee 

# Create your views here.
# def login_data(req):
#     if req.method=='POST':
#         e=req.GET.get()
def landing(req):
    return render(req,'landing.html')
def login(req):
    return render(req,'login.html')
def admindash(req):
    return render(req,'admindash.html')
def login_data(req):
    if req.method =='POST':
        e=req.POST.get('Email')
        p=req.POST.get('Password')
        if e=='admin@gmail.com' and p=='12345':
            data={
                'name':'Admin',
                'email':'admin@gmail.com',
                'contact':12345,
                'password':12345
            }
            req.session['user']='admin'
            req.session['data']=data 
            return redirect(req,'admindash')
        else:
            user=Employee.objects.filter(Email=e).first()
            if not user:
                return render(req,'login.html',{'massage':'email not register'})
def save_employee(req):
    if req.method=='POSST':
        Employee.objects.create(
            name=req.POST.get('name'),
            email=req.POST.get('email'),
            contact=req.POST.get('contact'),
            salary=req.POST.get('salary'),
            position=req.POST.get('position'),
         
        )
        return redirect('admindash')
    return redirect('admindash')
def forget(req):
    return render(req,'forget.html')
def employee_list(req):
    employees=Employee.objects.all().order_by('-id')#latest fisrt
    return render(req,'employee_list.html',{'employees':employees})
def all_employee(req):
     emp = employee.objects.all()

     employee= []
     for i in emp:
          employee.append({
             'id':i.id,
             'Name': i.Name,
              'Email': i.Email,
             'Contact': i.Contact,
              'Position': i.Department,
              'Salary': i.Salary,
         })
     
     return render(req,'all_employee.html',{'employee':employee})
def edit(req,pk):
    userdata=Employee.objects.get(id=pk)
    data={
            name=req.GET.get('name'),
            email=req.GET.get('email'),
            contact=req.GET.get('contact'),
            salary=req.GET.get('salary'),
            position=req.GET.get('position'),
    }
    return render(req,'update.html',{'data':data})

def delete(req,pk):
    if req.session.items():
        userdata=Employee.objects.get(id=pk)
        userdata.delete()
        return redirect('show_all_employee')
    else:
        return redirect('login')
    

