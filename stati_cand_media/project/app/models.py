from django.db import models

# Create your models here.
class Student(models.Model):
    Name=models.CharField(max_length=20)
    Image=models.ImageField(upload_to='images/')
    Audio=models.FileField(upload_to='audio/')
    Video=models.FileField(upload_to='video/')
    Document=models.FileField(upload_to='documents/')

