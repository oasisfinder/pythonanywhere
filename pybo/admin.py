# Register your models here.

from django.contrib import admin
from .models import Menu

#
# class MenuAdmin(admin.ModelAdmin):
#     search_fields = ['name']
# admin.site.register(Menu, MenuAdmin)


class MenuAdmin(admin.ModelAdmin):
    list_display = ('id','name','distance','type', 'price_display')
    def price_display(self, obj):
        return "{:,}".format(obj.price)
    price_display.short_description = 'Price'
admin.site.register(Menu, MenuAdmin)
