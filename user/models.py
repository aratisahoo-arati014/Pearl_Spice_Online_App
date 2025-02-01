
from types import NoneType
from django.db import models

# Create your models here.

class contactus(models.Model):


  Name=models.CharField(max_length=50,null=True)
  Email=models.EmailField(max_length=90,null=True)
  Mobile=models.CharField(max_length=22,null=True)
  Subject=models.CharField(max_length=200,null=True)
  Message=models.TextField(null=True)

  def __str__(self):
    return self.Name


class tbl_register(models.Model):
  name=models.CharField(max_length=50,null=True)
  email=models.EmailField(primary_key=True)
  mobile=models.CharField(max_length=20,null=True)
  password=models.CharField(max_length=200,null=True)
  pincode=models.CharField(max_length=20,null=True)
  city=models.CharField(max_length=50,null=True)
  address=models.TextField(max_length=50,null=True)
  picture=models.ImageField(upload_to='static/userpic/')



class tbl_category(models.Model):
  product_category=models.CharField(max_length=30,null=True)
  category_picture=models.ImageField(upload_to='static/category/',null=True)
  def __str__(self):
    return self.product_category


class tbl_product(models.Model):
  product_name=models.CharField(max_length=100,null=True)
  category=models.ForeignKey(tbl_category,on_delete=models.CASCADE)
  price=models.FloatField(null=True)
  discount_price=models.IntegerField(null=True)
  quantity=models.IntegerField(null=True)
  product_image=models.ImageField(upload_to='static/product/',null=True)

class tbl_slider(models.Model):
  slider_picture=models.ImageField(upload_to='static/slider/',null=True)
  title=models.CharField(max_length=200,null=True)
  description=models.TextField(null=True)



class tbl_cart(models.Model):
  userid=models.CharField(max_length=50,null=True)
  product_id=models.IntegerField()
  product_image=models.CharField(max_length=200,null=True)
  product_price=models.FloatField()
  quantity=models.IntegerField()
  total_price=models.FloatField()
  product_name=models.CharField(max_length=100,null=True)
  added_date=models.DateField(null=True)


class tbl_order(models.Model):
  userid=models.CharField(max_length=50,null=True)
  product_id=models.IntegerField()
  product_name=models.CharField(max_length=100,null=True)
  product_image=models.CharField(max_length=200,null=True)
  product_price=models.FloatField()
  product_quantity=models.IntegerField()
  total_price=models.FloatField()
  status=models.CharField(max_length=15,null=True)
  order_date=models.DateField(null=True)


class tbl_booktable(models.Model):
  name = models.CharField(max_length=50, null=True)
  email = models.EmailField(max_length=50, null=True)
  mobile = models.CharField(max_length=20, null=True)
  people = models.IntegerField( null=True)
  bookingdate = models.DateField(null=True)
  bookingtime = models.TimeField(null=True)
  eventtype = models.TextField(max_length=100, null=True)
  foodtype = models.TextField(max_length=100, null=True)
  booking_date = models.DateField(null=True)

