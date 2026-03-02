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

class CartDb(models.Model):
    Username=models.CharField(max_length=100,null=True,blank=True)
    Product_name = models.CharField(max_length=100, null=True, blank=True)
    Quantity=models.IntegerField(null=True,blank=True)
    Price=models.IntegerField(null=True,blank=True)
    Totalprice=models.IntegerField(null=True,blank=True)
    Product_image=models.ImageField(upload_to="Cart_Images",null=True,blank=True)

class OrderDb(models.Model):
    First_Name = models.CharField(max_length=100, null=True, blank=True)
    Last_Name  = models.CharField(max_length=100, null=True, blank=True)
    Email      = models.EmailField(max_length=100, null=True, blank=True)
    Place      = models.CharField(max_length=100, null=True, blank=True)
    Address    = models.CharField(max_length=100, null=True, blank=True)
    Mobile     = models.IntegerField(null=True, blank=True)
    State      = models.CharField(max_length=100, null=True, blank=True)
    Pin        = models.IntegerField(null=True, blank=True)
    TotalPrice = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return f"{self.First_Name} {self.Last_Name}"

