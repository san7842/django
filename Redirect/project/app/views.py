from django.shortcuts import render,redirect
from django.urls import reverse
from urllib.parse import urlencode


# Create your views here.

def myredirect(req):
    return redirect('https://www.google.com/?zx=1763215057510&no_sw_cr=1')

def myredirect1(req):
     return redirect(req,'home')
def home(req):
     return render(req,'home.html')

def myredirect2(req):
     base_url=reverse('home1')
     return redirect(req,base_url)
def home1(req):
     return render(req,'home1.html')

def myredirect3(req):
     base_url=reverse('home3')
     data=urlencode({'name':'sandeep'})
     return redirect(f'{base_url}?{data}')

def home3(req):
     return render(req,'home3.html')



