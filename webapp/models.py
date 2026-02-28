from django.db import models

# Create your models here.
class ContactDb(models.Model):
    Name=models.CharField(max_length=100,null=True,blank=True)
    Email = models.EmailField( null=True, blank=True)
    Message=models.TextField(null=True,blank=True)

class RegistrationDb(models.Model):
    username=models.CharField(max_length=100,null=True,blank=True)
    email = models.EmailField(max_length=100, null=True, blank=True)
    password = models.CharField(max_length=100, null=True, blank=True)
    password1= models.CharField(max_length=100, null=True, blank=True)
