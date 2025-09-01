
from django.db import models
from django.utils import timezone

from orders_app.models import Order


class Company(models.Model):
    eik = models.CharField(max_length=13, unique=True,)
    dds = models.CharField(max_length=20)
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    mol = models.CharField(max_length=100)
    recipient = models.CharField(max_length=100) # poluchatel
    added_at = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return f"{self.eik} - {self.name}"

class Invoice(models.Model):
    DDS = models.CharField(max_length=20, default='20')
    date = models.DateField(default=timezone.now)
    comment = models.TextField(default='', blank=True, null=True, max_length=500)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    whole_price_without_dds = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    whole_price_with_dds = models.DecimalField(max_digits=10, decimal_places=2, default = 0)
    cancelled = models.BooleanField(default=False)

    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='invoices')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='invoices')

    def __str__(self):
        return f'No.{self.id}'



