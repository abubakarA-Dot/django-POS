from django.db import models
from base.models.base import BaseEntity


class Category(BaseEntity):
   
   category_name = models.CharField(default=" ",max_length=122)
   product_id = models.IntegerField(default=0)
   name  = models.CharField(max_length=122,default="")
   parent = models.CharField(max_length=122,default="")
   status = models.IntegerField(default=0)
    
   def __str__(self):
        return self.category_name

   