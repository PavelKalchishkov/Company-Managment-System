
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

    def __str__(self):
        return self.name

class Invoice(models.Model):
    supplier_eik = models.CharField(max_length=13, default='000000000')
    supplier_dds = models.CharField(max_length=20, default='BG000000000')
    supplier_name = models.CharField(max_length=100, default='firma_firma')
    supplier_address = models.CharField(max_length=100,default='goce delchev 30')
    supplier_mol = models.CharField(max_length=100, default='Pavel Kalchishkov')
    supplier_phone_number = models.CharField(max_length=100, default='089 860 2996')
    supplier_email = models.CharField(max_length=100, default='pavelkalchishkov@gmail.com')

    DDS_CHOICES = [
        ('20', '20'),
        ('9', '9'),
        ('0', '0'),
    ]
    DDS = models.CharField(max_length=20, choices=DDS_CHOICES, default='20')
    date = models.DateField(default=timezone.now)
    comment = models.TextField(default='', blank=True, null=True, max_length=500)
    discount = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    whole_price_without_dds = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    whole_price_with_dds = models.DecimalField(max_digits=10, decimal_places=2, default = 0)

    company = models.ForeignKey(Company, on_delete=models.CASCADE, related_name='invoices')
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='invoices')

    def __str__(self):
        return f'No.{self.id}'



