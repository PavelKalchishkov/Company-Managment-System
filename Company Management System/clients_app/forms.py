from django import forms

from .models import Client

class ClientCreateForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'company': forms.Select(attrs={'class': 'select2'})
        }

        labels = {
            'personal_phone_number' : 'Personal phone number (optional)',
            'company' : 'Company (optional)',
            'address' : 'Address (optional)',
            'city' : 'City (optional)',
            'country' : 'Country (optional)',
            'province' : 'Province (optional)',
            'ZIP' : 'ZIP (optional)',
            'fax_number' : 'Fax number (optional)',
            'web_page' : 'Web page (optional)',
            'notes' : 'Notes (optional)',
        }
        exclude = ('added_at',)

class ClientUpdateForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'company': forms.Select(attrs={'class': 'select2'})
        }

        labels = {
            'personal_phone_number': 'Personal phone number (optional)',
            'company': 'Company (optional)',
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