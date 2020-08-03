from django.db import models

# Create your models here.
class File_Upload(models.Model):
    description     = models.CharField(max_length=255, blank=True)
    document        = models.FileField(upload_to='encode/')
    
    