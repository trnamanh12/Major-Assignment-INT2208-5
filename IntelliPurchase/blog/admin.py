from django.contrib import admin
from .models import Product, Post
# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = ['product_name']
    list_filter = ['product_name']
    search_fields = ['product_name']

admin.site.register(Product, ProductAdmin)

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'date']
    list_filter = ['date']
    search_fields = ['title']

admin.site.register(Post, PostAdmin)