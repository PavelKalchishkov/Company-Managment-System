import django_filters
from django import forms

from orders_app.models import Order, OrderProduct
from products_app.models import Product


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
    order_price = django_filters.RangeFilter()
    order_date = django_filters.DateFromToRangeFilter(
        widget=django_filters.widgets.RangeWidget(
            attrs={'type': 'date'}))

    class Meta:
        model = Order
        fields = '__all__'
        exclude = ('order_version','order_address', 'products')
