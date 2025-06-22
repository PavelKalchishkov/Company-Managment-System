import django_filters
from django import forms

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

class OrderUpdateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ('products', 'order_version', 'order_price')

class OrderProductForm(forms.ModelForm):
    class Meta:
        model = OrderProduct
        fields = ['id', 'product', 'quantity']

class OrderViewFilter(django_filters.FilterSet):
    payment_method = django_filters.ChoiceFilter(
        choices=Order._meta.get_field('payment_method').choices,
        widget=forms.Select(attrs={
            'class': 'select2',
            'data-placeholder': 'Payment'
        })
    )

    order_status = django_filters.ChoiceFilter(
        choices=Order._meta.get_field('order_status').choices,
        widget=forms.Select(attrs={
            'class': 'select2',
            'data-placeholder': 'Status'
        })
    )

    client = django_filters.ModelChoiceFilter(
        queryset=Client.objects.all(),
        widget=forms.Select(attrs={
            'class': 'select2',
            'data-placeholder': 'Client'
        })
    )

    employee = django_filters.ModelChoiceFilter(
        queryset=Employee.objects.all(),
        widget=forms.Select(attrs={
            'class': 'select2',
            'data-placeholder': 'Employee'
        })
    )

    shipper = django_filters.ModelChoiceFilter(
        queryset=Shipper.objects.all(),
        widget=forms.Select(attrs={
            'class': 'select2',
            'data-placeholder': 'Shipper'
        })
    )

    class Meta:
        model = Order
        fields = '__all__'
        exclude = ('order_version','order_address', 'products')
