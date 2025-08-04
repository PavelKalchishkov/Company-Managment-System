from django.db import models

class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.FloatField()
    length = models.FloatField()
    weight = models.FloatField()
    color = models.CharField(max_length=100)
    vendor = models.ForeignKey('vendors_app.Vendor',
                               on_delete=models.CASCADE,
                               related_name='products')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name
