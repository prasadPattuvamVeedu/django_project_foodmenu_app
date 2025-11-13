from django.db import models

class Item(models.Model):
    def __str__(self):
        return f"{self.Item_Name}"
        
        
    Item_Name = models.CharField(max_length=200)
    Item_desc = models.CharField(max_length=200)
    Item_price = models.IntegerField()
   