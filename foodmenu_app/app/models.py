from django.db import models

class Item(models.Model):
    def __str__(self):
        return f"{self.Item_Name}"
        
        
    Item_Name = models.CharField(max_length=200)
    Item_desc = models.CharField(max_length=200)
    Item_price = models.IntegerField()
    Item_image=models.CharField(max_length=500,default="https://th.bing.com/th/id/OIP.NULWEmlj4g8ASx3w_Ps7MQAAAA?w=155&h=180&c=7&r=0&o=7&dpr=1.3&pid=1.7&rm=3")
   