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

