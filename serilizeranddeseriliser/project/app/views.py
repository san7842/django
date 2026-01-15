from django.shortcuts import render
from .models import Student
from .serializers import Student1

# Create your views here.
def stu_list(req):
    data=Student1.objects.all()
    serialiser=Student1(data,many=True)
    print(serialiser)
    print(serialiser.data)
