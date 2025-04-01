from django.db import models
from django.contrib.postgres.fields import ArrayField


class Vendor(models.Model):
    name = models.CharField(max_length=100,
                            default="new_vendor")

    products = ArrayField(models.IntegerField(),
                          null=True,
                          blank=True,
                          default=list)

    additional_information = models.TextField(max_length=500,
                                              default='')
