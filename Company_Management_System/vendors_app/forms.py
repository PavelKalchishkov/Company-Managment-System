from django import forms
from .models import Vendor


class VendorCreationForm(forms.ModelForm):
    class Meta:
        model = Vendor
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

class VendorUpdateForm(forms.ModelForm):
    class Meta:
        model = Vendor
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