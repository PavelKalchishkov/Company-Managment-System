from django import forms

from orders_app.models import Order, OrderProduct


class OrderCreationForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ('products',)

class OrderUpdateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        exclude = ('products',)

class OrderProductForm(forms.ModelForm):
    class Meta:
        model = OrderProduct
        fields = ['id', 'product', 'quantity']