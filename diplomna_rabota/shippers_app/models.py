from django.db import models
from django.contrib.postgres.fields import ArrayField


class Shipper(models.Model):
    name = models.CharField(max_length=100),
    salary = models.IntegerField(),
    current_products_being_shipped = ArrayField(models.IntegerField(),
                                                null=True,
                                                blank=True,)