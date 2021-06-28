from io import SEEK_CUR
from django.contrib import admin
from django.db import models
from django.db.models.base import ModelState
from django.db.models.deletion import CASCADE
from django.db.models.fields import EmailField
from django.db.models.query_utils import select_related_descend

# Create your models here.


class Product(models.Model):
    product_id = models.AutoField
    product_name = models.CharField(max_length=30)
    category = models.CharField(max_length=30,default='')
    subcategory = models.CharField(max_length=30,default='')
    price = models.IntegerField(default=0)
    description = models.CharField(max_length=300)
    pub_date = models.DateField()
    image = models.ImageField(upload_to='Esite/imge',default='')
    image2 = models.ImageField(upload_to='Esite/imge',default='')

    def __str__(self):
        return self.product_name

class mainImage(models.Model):
    imageId = models.AutoField
    image = models.ImageField(upload_to='Esite/imge', default='Esite/image/game.jpg')
    headding = models.CharField(max_length=30,default='')
    subheadding = models.CharField(max_length=40,default='')

    def __str__(self):
        return self.headding

class Contact(models.Model):
    msg_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    email = models.CharField(max_length=30,default='')
    phone = models.IntegerField(default=123456789101)
    description = models.CharField(max_length=509,default='')
    
    def __str__(self):
        return f"{self.name}  {self.email} {self.phone}"


class Order(models.Model):
    order_id = models.AutoField(primary_key=True)
    item_JSON = models.CharField(max_length=300)
    name = models.CharField(max_length=50,null=False)
    email = models.CharField(max_length=30,null=False)
    phone = models.IntegerField(default=123456789101,null=False)
    address = models.CharField(max_length=100,)
    city = models.CharField(max_length=20)
    state = models.CharField(max_length=20)
    zip_code = models.IntegerField(default=0000)

    def __str__(self):
        return f"{self.name} {self.email} {self.phone}"

class updateOrder(models.Model):
    update_id = models.AutoField(primary_key=True)
    order_id = models.IntegerField()
    update_desc = models.CharField(max_length=500)
    timeStamp = models.DateField(auto_now_add=True)

    def __str__(self):
        return f'{self.update_id} {self.order_id} {self.update_desc[0:15]} '