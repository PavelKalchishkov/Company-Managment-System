from django import forms

from .models import Product

class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'length', 'weight', 'color', 'vendor']

class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'length', 'weight', 'color', 'vendor']