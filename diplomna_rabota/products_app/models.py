from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    length = models.FloatField()
    weight = models.FloatField()
    color = models.CharField(max_length=100)
    manufacturer = models.CharField(max_length=100)
