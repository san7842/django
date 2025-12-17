from django.db import models

# Create your models here.   
class Employee(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.EmailField()
    Contact=models.IntegerField()
    Salary=models.FloatField()
    position=models.CharField(max_length=20)
    def __str__(self):
        return self.name +" "+self.email