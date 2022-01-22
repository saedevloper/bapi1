from django.contrib import admin

from .models import *


class ProductsAdmin(admin.ModelAdmin):
    list_display = ['name', 'description1', 'description2', 'description3', 'description4', 'description5',
                    'description6', 'description7', 'description8', 'description9', 'description10']


admin.site.register(Products, ProductsAdmin)


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['title']


admin.site.register(Category, CategoryAdmin)
