from django.db import models
from django.conf import settings

# Create your models here.
class Product(models.Model):
    product_id = models.AutoField(primary_key=True)
    product_name = models.CharField(max_length=100)
    category_id = models.IntegerField() 
    TGDD_product_link = models.URLField()
    FPT_product_link = models.URLField()
    image = models.URLField()

    def __str__(self):
        return self.product_name
    
    class Meta:
        db_table = 'product'

class ProductSpec(models.Model):
    id = models.AutoField(primary_key=True)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    color = models.CharField(max_length=100)
    screen = models.CharField(max_length=100)
    rear_camera = models.CharField(max_length=100)
    front_camera = models.CharField(max_length=100)
    OS_CPU = models.CharField(max_length=100)
    memory_storage = models.CharField(max_length=100)
    ket_noi = models.CharField(max_length=100)
    pin_sac = models.CharField(max_length=100)
    tien_ich = models.CharField(max_length=100)
    thongtin_chung = models.CharField(max_length=100)

    def __str__(self):
        return self.product.product_name

    class Meta:
        db_table = 'technical_details'

class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.title
    
class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    body = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

from django.contrib import admin

# Register your models here.
from .models import Post, Comment

# Register your models here.
class CommentInline(admin.StackedInline):
    model = Comment
