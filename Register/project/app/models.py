from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    contact=models.IntegerField()
    details=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image/')
