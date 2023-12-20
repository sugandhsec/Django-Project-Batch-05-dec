from django.db import models
from app_buyer.models import *
# Create your models here.
class Category(models.Model):
    cname=models.CharField(max_length=200)
    cdescription=models.TextField(max_length=500)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    def __str__(self) :
        return self.cname 
    
class Product(models.Model):
    pname=models.CharField(max_length=200)
    price=models.IntegerField()
    image=models.FileField(upload_to="product/")
    description =models.TextField(max_length=500)
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    category=models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self) :
        return self.pname
    
