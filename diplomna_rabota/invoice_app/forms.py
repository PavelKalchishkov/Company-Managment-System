from django import forms

from .models import Company, Invoice


class CompanyCreateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'

class CompanyUpdateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'

class InvoiceCreateForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'
        exclude = ('whole_price_without_dds', 'whole_price_with_dds')

class InvoiceUpdateForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'