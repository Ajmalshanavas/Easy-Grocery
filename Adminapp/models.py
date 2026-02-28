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