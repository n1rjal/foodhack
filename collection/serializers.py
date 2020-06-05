from rest_framework import serializers
from . import models

class WareHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.WareHouse
        ordering="name"
        fields=['name','place','district','latitude','longitude','item']

class ListWareHouseSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.WareHouse
        ordering="name"
        fields=['name','place','district','latitude','longitude']


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model=models.Item
        fields=['name','wprice','rprice','unit']