from django import forms

from .models import Shipper


class ShipperCreationForm(forms.ModelForm):
    class Meta:
        model = Shipper
        fields = ['name', 'salary', 'phone_number']


class ShipperUpdateForm(forms.ModelForm):
    class Meta:
        model = Shipper
        fields = ['name', 'salary', 'phone_number']