from django.db import models
from django.core.validators import MinValueValidator

# Create your models here.


class Item(models.Model):
    # wpirce and rprice means wholesale and retail
    name=models.CharField(max_length=20)
    wprice=models.IntegerField(validators=[MinValueValidator(0)])
    rprice=models.IntegerField(validators=[MinValueValidator(0)])
    unit=models.CharField(max_length=10)
    
    def __str__(self):
        return (self.name)


class WareHouse(models.Model):
    name=models.CharField(max_length=30,unique=True)
    place=models.CharField(max_length=30)
    district=models.CharField(max_length=30)
    latitude=models.CharField(max_length=10)
    longitude=models.CharField(max_length=10)
    item=models.ManyToManyField(Item)
    
    def itemcount(self):
        itemcount= self.item.count()
        return (itemcount)   

    def __str__(self):
        return (self.name)
