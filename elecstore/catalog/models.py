from django.db import models

# Create your models here.

class ProductDirectory(models.Model):
    directory_name = models.CharField(max_length=200)
    #total_items = models.DateTimeField('date published')
    total_items = models.IntegerField(default=0)
    def __str__(self):              # __unicode__ on Python 2
        return self.directory_name


class ProductItem(models.Model):
    product_directory = models.ForeignKey(ProductDirectory)
    product_name = models.CharField(max_length=200)
    product_description = models.TextField()
    product_price = models.DecimalField(max_digits=8, decimal_places=2)
    def __str__(self):              # __unicode__ on Python 2
        return self.product_name
