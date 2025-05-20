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
        exclude = ['date']

class InvoiceUpdateForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'
        exclude = ['date']