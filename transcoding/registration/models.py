from django.db import models

# Create your models here.
class User_Profile(models.Model):
    username= models.CharField(max_length = 150)
    first_name= models.CharField(max_length = 150)
    last_name = models.CharField(max_length = 150)
    email  = models.EmailField()
    password = models.CharField(max_length = 150)

    
    
    
    
    