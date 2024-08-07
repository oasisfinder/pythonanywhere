# Register your models here.

from django.contrib import admin
from .models import Menu, Memo

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

class MemoAdmin(admin.ModelAdmin):
    list_display = ('title', 'status')  # 리스트에 표시할 필드
    list_filter = ('status',)  # 필터 옵션
    search_fields = ('title', 'status')  # 검색 가능한 필드

# Memo 모델을 admin에 등록
admin.site.register(Memo, MemoAdmin)