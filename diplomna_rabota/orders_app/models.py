import datetime
from django.db import models

class Order(models.Model):
    order_date = models.DateField(default=datetime.date.today)
    order_address = models.CharField(max_length=100)
    order_version = models.SmallIntegerField(default=1)

    products = models.ManyToManyField('products_app.Product',
                                     through='OrderProduct',
                                     related_name='orders')

    client = models.ForeignKey('clients_app.Client',
                               on_delete=models.SET_NULL,
                               null=True,
                               blank=True,
                               related_name='orders')

    employee = models.ForeignKey('employees_app.Employee',
                                 on_delete=models.SET_NULL,
                                 null=True,
                                 blank=True,
                                 related_name='orders')

    shipper = models.ForeignKey('shippers_app.Shipper',
                                on_delete=models.SET_NULL,
                                null=True,
                                blank=True,
                                related_name='orders')


class OrderProduct(models.Model):
    order = models.ForeignKey('orders_app.Order', on_delete=models.CASCADE)
    product = models.ForeignKey('products_app.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


