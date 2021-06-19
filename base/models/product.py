from django.db import models
from django.db.models.deletion import CASCADE
from django.db.models.fields import AutoField, FloatField
from base.models.base import BaseEntity
from base.models.category import Category
from datetime import datetime

# order by user
class Product(BaseEntity):
  
    product_name = models.CharField(max_length=180,null=True)
    Quantity = models.CharField(max_length=122,default=0)
    Price = FloatField(default=0)
    expiry_date = models.DateField(default=datetime.today)
    manufactor_date = models.DateField(default=datetime.today)
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='product',default=0)
    datetime = models.DateField(default=datetime.today)
    description = models.TextField(max_length=500)
    stock = models.IntegerField(default=0)
    count_sold = models.IntegerField(default=0)

    def __str__(self):
         return self.product_name
