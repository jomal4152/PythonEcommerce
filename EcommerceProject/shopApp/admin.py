from django.contrib import admin

# Register your models here.

from .models import Category, Products


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['cname', 'cslug']
    prepopulated_fields = {'cslug': ('cname',)}


admin.site.register(Category, CategoryAdmin)


class ProductAdmin(admin.ModelAdmin):
    list_display = ['pname', 'price', 'stock', 'available', 'created', 'updated']
    list_editable = ['price', 'stock', 'available']
    prepopulated_fields = {'pslug': ('pname',)}
    list_per_page = 20


admin.site.register(Products, ProductAdmin)
