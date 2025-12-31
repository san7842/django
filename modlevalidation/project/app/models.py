from django.db import models
# from django.core.validators import MinLengthValidator,MaxLengthValidator
from django.core.exceptions import ValidationError

# Create your models here.
def Validators_name(value):
    if len(value)<3 or len(value)>20:
        raise ValidationError("name length should be between 2 to 20 character")
    elif not value.isalpha():
        raise ValidationError("name should be only alphabetic character")
def validators_roll(value):
    if value<=0:
        raise ValidationError("Roll number should be a positive integer")
    elif value <1000 or value >9999:
        raise ValidationError("Roll number should  be not ")
class Student(models.Model):
    name=models.CharField(max_length=100,validators=[Validators_name])
    city=models.CharField(max_length=100)
    roll=models.IntegerField(validators=[validators_roll])
    def __str__(self):
        return self.name

