from rest_framework import  serializers

class Student1(serializers.Serializer):
    name=serializers.CharField()
    email=serializers.EmailField()
    city=serializers.CharField()