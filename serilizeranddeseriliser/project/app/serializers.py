from rest_framework import  serializers
from .models import Student

class Student1(serializers.Serializer):
    name=serializers.CharField()
    email=serializers.EmailField()
    city=serializers.CharField()

    def create(self, validated_data):
        return Student.objects.create(**validated_data)
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.email = validated_data.get('email', instance.email)
        instance.city = validated_data.get('city', instance.city)
        instance.save()
        return instance