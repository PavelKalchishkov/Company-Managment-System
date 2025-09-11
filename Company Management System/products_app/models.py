from django.db import models
from common.validators import PositiveFloatValidator

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField(validators=[PositiveFloatValidator()])
    length = models.FloatField(validators=[PositiveFloatValidator()])
    weight = models.FloatField(validators=[PositiveFloatValidator()])
    color = models.CharField(max_length=100)
    vendor = models.ForeignKey('vendors_app.Vendor',
                               on_delete=models.CASCADE,
                               related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
