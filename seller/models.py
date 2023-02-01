from django.db import models

# Create your models here.
class sellerregister_tb(models.Model):
    name=models.CharField(max_length=20)
    address=models.CharField(max_length=20)
    gender=models.CharField(max_length=20)
    dob=models.CharField(max_length=20)
    country=models.CharField(max_length=20)
    phonenumber=models.CharField(max_length=20)
    username=models.CharField(max_length=20)
    password=models.CharField(max_length=20)
    image=models.FileField()
    status=models.CharField(max_length=20,default="pending")
class product_tb(models.Model):
    productname=models.CharField(max_length=20)
    file=models.FileField()
    stock=models.CharField(max_length=20)
    price=models.IntegerField()
    details=models.CharField(max_length=20)
    sellerid=models.ForeignKey(sellerregister_tb,on_delete=models.CASCADE)
    categoryid=models.ForeignKey("siteadmin.category_tb",on_delete=models.CASCADE)
class tracking_tb(models.Model):
    orderid=models.ForeignKey("buyer.order_tb",on_delete=models.CASCADE)
    date=models.CharField(max_length=20)
    time=models.CharField(max_length=20)
    details=models.CharField(max_length=20)
