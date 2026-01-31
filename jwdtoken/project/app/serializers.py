from rest_framework import serializers # import after installetion  pip install djangorestframework
from .models import Student

class Stu_Serializers(serializers.ModelSerializer):
    class Meta:
        model=Student
        fields='__all__'