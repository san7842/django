from django.shortcuts import render
# def myrender(req):
#     return render(req,'new.html')


def myrender(req):
    email='sandeep@gmail.com'
    name='sandeep'
    data={'n':name,'e':email}
    return render(req,'new.html',data)
# Create your views here.
