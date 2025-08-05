from django import forms

from .models import Shipper


class ShipperCreationForm(forms.ModelForm):
    class Meta:
        model = Shipper
        fields = '__all__'
        labels = {
            'personal_phone_number': 'Personal phone number (optional)',
            'address': 'Address (optional)',
            'city': 'City (optional)',
            'country': 'Country (optional)',
            'province': 'Province (optional)',
            'ZIP': 'ZIP (optional)',
            'fax_number': 'Fax number (optional)',
            'web_page': 'Web page (optional)',
            'notes': 'Notes (optional)',
        }
        exclude = ('added_at',)


class ShipperUpdateForm(forms.ModelForm):
    class Meta:
        model = Shipper
        fields = '__all__'
        labels = {
            'personal_phone_number': 'Personal phone number (optional)',
            'address': 'Address (optional)',
            'city': 'City (optional)',
            'country': 'Country (optional)',
            'province': 'Province (optional)',
            'ZIP': 'ZIP (optional)',
            'fax_number': 'Fax number (optional)',
            'web_page': 'Web page (optional)',
            'notes': 'Notes (optional)',
        }
        exclude = ('added_at',)