from django.shortcuts import render
from django.http import HttpResponse
def landing(req):
    print("my first django project")
    return HttpResponse("<h1  style='color:red;'>welcome</h1>")
# Create your views here.
