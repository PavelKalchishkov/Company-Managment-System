from django import forms
from .models import Vendor
from django.utils.translation import gettext_lazy as _


class VendorCreationForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'
        labels = {
            'first_name': _('First Name'),
            'last_name': _('Last Name'),
            'phone_number': _('Phone number'),
            'personal_phone_number': _('Personal phone number (optional)'),
            'email': _('Email'),
            'job_title': _('Job title'),
            'address': _('Address (optional)'),
            'city': _('City (optional)'),
            'country': _('Country (optional)'),
            'province': _('Province (optional)'),
            'ZIP': _('ZIP (optional)'),
            'fax_number': _('Fax number (optional)'),
            'web_page': _('Web page (optional)'),
            'notes': _('Notes (optional)'),
        }
        exclude = ('added_at',)

class VendorUpdateForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'
        labels = {
            'first_name': _('First Name'),
            'last_name': _('Last Name'),
            'phone_number': _('Phone number'),
            'personal_phone_number': _('Personal phone number (optional)'),
            'email': _('Email'),
            'job_title': _('Job title'),
            'address': _('Address (optional)'),
            'city': _('City (optional)'),
            'country': _('Country (optional)'),
            'province': _('Province (optional)'),
            'ZIP': _('ZIP (optional)'),
            'fax_number': _('Fax number (optional)'),
            'web_page': _('Web page (optional)'),
            'notes': _('Notes (optional)'),
        }
        exclude = ('added_at',)