from django.db import models
from cloudinary_storage.storage import MediaCloudinaryStorage,RawMediaCloudinaryStorage,VideoMediaCloudinaryStorage

# Create your models here.
class Student(models.Model):
    Image=models.ImageField(upload_to='image',storage=MediaCloudinaryStorage())
    Video=models.FileField(upload_to='video',storage=VideoMediaCloudinaryStorage())
    Audio=models.FileField(upload_to='audio',storage=VideoMediaCloudinaryStorage())
    File=models.FileField(upload_to='file',storage=RawMediaCloudinaryStorage())
