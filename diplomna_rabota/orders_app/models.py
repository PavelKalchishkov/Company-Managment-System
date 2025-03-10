from django.db import models


class Order(models.Model):
    order_date = models.DateField()
    order_address = models.CharField(max_length=100)
    order_price = models.DecimalField(max_digits=10,
                                      decimal_places=2)

    supplier_id = models.CharField(max_length=100) # fix after adding supplier app

    product_id = models.CharField(max_length=100) # fix after adding products app

    client_id = models.ForeignKey(to='clients_app.Client',
                                  on_delete=models.CASCADE,
                                  related_name='client_id',
                                  null=True,
                                  blank=True)

    client_contact = models.CharField(max_length=100)