from django.db import models

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