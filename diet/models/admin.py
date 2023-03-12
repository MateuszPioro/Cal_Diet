from django.contrib import admin
from .models import Diary,Product

@admin.register(Diary)
class DiaryAdmin(admin.ModelAdmin):
    search_fields=['name']
    list_display=['id','name','date','calories']
    list_filter=['name','date']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    search_fields=['name']
    list_display=['id','name','calories']
    list_filter=['name']

 
 