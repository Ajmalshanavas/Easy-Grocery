from django.db import models

# Create your models here.
class CategoryDb(models.Model):
    CategoryName=models.CharField(max_length=100,unique=True)
    Description = models.TextField()
    CategoryImage=models.ImageField(upload_to='categories',blank=True,
    null=True)

    def __str__(self):
        return self.CategoryName

class ProductDb(models.Model):
    Category_name=models.CharField(max_length=100)
    Product_name=models.CharField(max_length=100,unique=True)
    Price=models.IntegerField()
    Description=models.TextField()
    ProductImage=models.ImageField(upload_to='products')

    def __str__(self):
        return self.Product_name



class ServiceDb(models.Model):
    Service_name  = models.CharField(max_length=200, null=True, blank=True)
    Description   = models.TextField(null=True, blank=True)
    Icon          = models.CharField(max_length=100, null=True, blank=True, help_text="Font Awesome icon class e.g. fa-truck")
    ServiceImage  = models.ImageField(upload_to='service_images/', null=True, blank=True)

    def __str__(self):
        return self.Service_name
