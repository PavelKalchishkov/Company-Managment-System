import datetime
from django.db import models

class Order(models.Model):
    order_date = models.DateField(default=datetime.date.today)
    order_address = models.CharField(max_length=100)
    order_version = models.SmallIntegerField(default=1)
    order_price = models.DecimalField(max_digits=10, decimal_places=2, default=0)

    PAYMENT_CHOICES = [
        ('cash', 'cash'),
        ('card', 'card'),
        ('bank transfer', 'bank transfer'),
        ('other', 'other'),
    ]
    payment_method = models.CharField(max_length=15,
                                      choices=PAYMENT_CHOICES,
                                      default='cash')


    STATUS_ORDER_CHOICES = [
        ('pending', 'pending'),
        ('delivered', 'delivered'),
        ('canceled', 'canceled'),
    ]
    order_status = models.CharField(max_length=15,
                                    choices=STATUS_ORDER_CHOICES,
                                    default='pending')

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

    def __str__(self):
        return f'{self.id}'


class OrderProduct(models.Model):
    order = models.ForeignKey('orders_app.Order', on_delete=models.CASCADE)
    product = models.ForeignKey('products_app.Product', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)


