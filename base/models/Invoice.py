from django.db import models
from datetime import datetime
from django.db.models.deletion import CASCADE

from django.db.models.fields import AutoField
from base.models.base import BaseEntity
from base.models.category import Category
from base.models import Tag,Product,Category
from django.contrib.auth.models import User

class Event(models.Model):
    event_name = models.CharField(default="",max_length=122)
    def __str__(self):
        return self.event_name

class Invoice(BaseEntity):
    Product_id = models.ForeignKey(Product,max_length=122,on_delete=models.CASCADE,default=1)
    Event_Name = models.ForeignKey(Event,on_delete=CASCADE)
    sold_Quantity = models.IntegerField(default=0)
    price = models.FloatField(default=0,null=True)
    total_price = models.FloatField(default=0, null = True)
    date_time = models.DateField(default=datetime.today)
    
    def __str__(self):
        return self.Product_id.product_name+" "+str((self.date_time))