from django.db import models

# Create your models here.
class Student(models.Model):
    Name=models.CharField(max_length=50)
    Email=models.EmailField()
    Contact=models.IntegerField()
    Details=models.CharField(max_length=100)
    Image=models.ImageField(upload_to='image/')

    def __str__(self):
        return self.name +" "+self.email
    # def __str__(self):
    #     return str(self.contact)
