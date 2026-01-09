from django.db import models

# Create your models here.
class Movies(models.Model):
    name=models.CharField(max_length=50)
    dis=models.TextField()
    active=models.BooleanField()

    def __str__(self):
        return self.name