from django import forms
from .models import Vendor


class VendorCreationForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['name', 'additional_information']

class VendorUpdateForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = ['name', 'additional_information']