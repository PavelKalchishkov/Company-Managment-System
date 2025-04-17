from django import forms

from orders_app.models import Order


class OrderCreationForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'

class OrderUpdateForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'