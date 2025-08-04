from django import forms

from .models import Shipper


class ShipperCreationForm(forms.ModelForm):
    class Meta:
        model = Shipper
        fields = '__all__'
        exclude = ('added_at',)


class ShipperUpdateForm(forms.ModelForm):
    class Meta:
        model = Shipper
        fields = '__all__'
        exclude = ('added_at',)