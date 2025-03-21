from django.db import models
from django.contrib.postgres.fields import ArrayField

from common.validators import AllNumbersValidator, TenCharactersValidator


class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=100,
                                    validators=[AllNumbersValidator,
                                                TenCharactersValidator])
    email = models.EmailField(unique=True)
    address = models.CharField(max_length=100)
    orders = ArrayField(models.IntegerField(), blank=True, default=list) # list of the order id's

