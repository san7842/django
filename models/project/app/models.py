from django.db import models

# Create your models here.
class Aadhar(models.Model):
    Aadharno=models.IntegerField()
    Created_date=models.DateField(auto_now=True)
    Created_by=models.CharField(max_length=50)
    def __str__(self):
        return str(self.Aadharno)
class Student(models.Model):
    stu_name=models.CharField(max_length=100)
    stu_email=models.EmailField(unique=True)
    stu_contact=models.IntegerField()
    stu_aadhar=models.OneToOneField(Aadhar,on_delete=models.CASCADE)

    def __str__(self):
        return str.stu_name
