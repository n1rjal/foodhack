from django.contrib import admin
from . import models

# Register your models here.
admin.site.site_header="WareHouse Admin"

class ItemAdmin(admin.ModelAdmin):    
    list_display=('name','RetailPrice','WholeSalePrice','LeftOver')
    search_fields=('name',)
    def RetailPrice(self,obj):
        return "Rs{}".format(obj.rprice)

    def WholeSalePrice(self,obj):
        return "Rs{}".format(obj.wprice)

    def LeftOver(self,obj):
        return "{}{}".format(obj.leftover,obj.unit)


admin.site.register(models.Item,ItemAdmin)

class WareHouseAdmin(admin.ModelAdmin):
    list_display=('name','Address','TotalItems')
    search_fields=("name",)
    def Address(self,obj):
        return "{}, {}".format(obj.place,obj.district)

    def TotalItems(self,obj):
        return "{}".format(obj.itemcount())

admin.site.register(models.WareHouse,WareHouseAdmin)