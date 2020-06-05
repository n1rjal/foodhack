from django.shortcuts import render
from django.shortcuts import HttpResponse
from . import models
from . import serializers

from rest_framework.response import Response
from rest_framework.decorators import api_view

import requests,json

#python functions here

apikey="563492ad6f917000010000014fe5a87d41324425a8f78c78dbe3449d"

def imagesearch(query):
    try:
        url="https://api.pexels.com/v1/search"
        data={"query":query,"per_page":"1"}
        headers={}
        print(data)
        apikey="563492ad6f917000010000014fe5a87d41324425a8f78c78dbe3449d"
        headers['Authorization']=apikey
        req=requests.get(url,params=data,headers=headers)
        resp=req.json()
        resp=resp['photos'][0]
        resp=resp['src']
        return resp
    except Exception as e:
        return {"error":"Something went wrong","code":str(e)}

def item(pk):
    item=models.Item.objects.get(id=pk)
    
    result=serializers.ItemSerializer(item).data
    result['photo']=imagesearch(item.name)

    return result

# Create your views here.
def home(request):
    return HttpResponse("<h1>Requested to go to admin</h1>")

@api_view(['GET'])
def allitems(request):
    items=models.Item.objects.all()
    if request.method=="GET":
        items=serializers.ItemSerializer(items,many=True)
        return Response(items.data)

@api_view(['GET'])
def allwarehouse(request):
    allwarehouses=models.WareHouse.objects.all()
    if request.method=="GET":
        allwarehouses=serializers.ListWareHouseSerializer(allwarehouses,many=True)
        data=allwarehouses.data
        return Response(data)

@api_view(['GET'])
def warehouse(request,name):
    ware=models.WareHouse.objects.filter(name=name).first()
    if request.method=="GET":
        if ware is not None:
            ware=serializers.WareHouseSerializer(ware,many=False)
            ware=ware.data

            items=ware['item']
            itemsdata=[]
            
            for each_item in items:
                itemsdata.append(item(each_item))
            
            ware['item']=itemsdata
            return Response(ware)
        else:
            return Response({"error":"Not found"})