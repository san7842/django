from django.db import models

# Create your models here.
class Student(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField()
    contact=models.IntegerField()
    details=models.CharField(max_length=100)
    image=models.ImageField(upload_to='image/')

    def __str__(self):
        return self.name +" "+self.email
    # def __str__(self):
    #     return str(self.contact)