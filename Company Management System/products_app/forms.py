from django import forms
from .models import Product
from django.utils.translation import gettext_lazy as _


class ProductCreateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'length', 'weight', 'color', 'vendor']

        labels = {
            'name': _('name'),
            'price': _('price'),
            'length': _('length'),
            'weight': _('weight'),
            'color': _('color'),
            'vendor': _('vendor')
        }

class ProductUpdateForm(forms.ModelForm):
    class Meta:
        model = Product
        fields = ['name', 'price', 'length', 'weight', 'color', 'vendor']

        labels = {
            'name': _('name'),
            'price': _('price'),
            'length': _('length'),
            'weight': _('weight'),
            'color': _('color'),
            'vendor': _('vendor')
        }