from django.db import models

# Create your models here.

"""
product
-nom 
-prix
-quantité 
-description 
-image

"""
class product(models.Model):
        name =models.CharField(max_length=128)
        price = models.FloatField(default=0.0)
        quantité = models.IntegerField(default=0) 
        description = models.TextField(blank=True)
        thumbnail = models.ImageField(upload_to="products", blank=True, null=True)

        def __str__(self):
           return self.name 