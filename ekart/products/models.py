from django.db import models

# Create your models here.

class Featured_Product(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    image = models.ImageField(upload_to='featured_images/')


class New_arrival(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    image = models.ImageField(upload_to='newarrival_images/')