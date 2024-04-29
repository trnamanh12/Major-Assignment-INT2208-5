from django.contrib import admin
from .models import Product
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name']
    list_filter = ['product_name']
    search_fields = ['product_name']

admin.site.register(Product, ProductAdmin)