from django.shortcuts import render
from .models import Student
from .serializers import Stu_Serializers
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated

# Create your views here.
from rest_framework import viewsets

class StudentViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUser]
    """
    A simple ViewSet for viewing and editing accounts.
    """
   
    queryset = Student.objects.all()
    serializer_class = Stu_Serializers
