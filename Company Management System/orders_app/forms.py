import django_filters
from django import forms
from django.utils.translation import gettext_lazy as _

from clients_app.models import Client
from orders_app.models import Order, OrderProduct
from products_app.models import Product
from shippers_app.models import Shipper
from employees_app.models import Employee


class OrderCreationForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ('products','order_version', 'order_price')

        labels = {
            'order_date': _('Order Date'),
            'order_address': _('Order Address'),
            'payment_method': _('Payment Method'),
            'order_status': _('Order Status'),
            'client': _('Client'),
            'employee': _('Employee'),
            'shipper': _('Shipper'),
        }

class OrderUpdateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ('products', 'order_version', 'order_price')

        labels = {
            'order_date': _('Order Date'),
            'order_address': _('Order Address'),
            'payment_method': _('Payment Method'),
            'order_status': _('Order Status'),
            'client': _('Client'),
            'employee': _('Employee'),
            'shipper': _('Shipper'),
        }

class OrderProductForm(forms.ModelForm):
    class Meta:
        model = OrderProduct
        fields = ['id', 'product', 'quantity']

        labels = {
            'product': _('Product'),
            'quantity': _('Quantity'),
        }

class OrderViewFilter(django_filters.FilterSet):
    payment_method = django_filters.ChoiceFilter(
        choices=Order._meta.get_field('payment_method').choices,
        widget=forms.Select(
            attrs={
            'class': 'select2',
            'data-placeholder': _('Payment')
        })
    )

    order_status = django_filters.ChoiceFilter(
        choices=Order._meta.get_field('order_status').choices,
        widget=forms.Select(attrs={
            'class': 'select2',
            'data-placeholder': _('Status')
        })
    )

    client = django_filters.ModelChoiceFilter(
        queryset=Client.objects.all(),
        widget=forms.Select(attrs={
            'class': 'select2',
            'data-placeholder': _('Client')
        })
    )

    employee = django_filters.ModelChoiceFilter(
        queryset=Employee.objects.all(),
        widget=forms.Select(attrs={
            'class': 'select2',
            'data-placeholder': _('Employee')
        })
    )

    shipper = django_filters.ModelChoiceFilter(
        queryset=Shipper.objects.all(),
        widget=forms.Select(attrs={
            'class': 'select2',
            'data-placeholder': _('Shipper')
        })
    )

    class Meta:
        model = Order
        fields = '__all__'
        exclude = ('order_version','order_address', 'products')
