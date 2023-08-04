from django.db import models

# Create your models here.
class Item(models.Model):
    
    def __str__(self):
        return self.item_name
    
    item_name=models.CharField(max_length=200) ##item name
    item_desc=models.CharField(max_length=200) ##item description
    item_price=models.IntegerField()           ##item cost
      ##item image with default logo
    item_image = models.CharField(max_length=500,default="")
    
