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
    added_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

