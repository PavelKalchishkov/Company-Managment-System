from django import forms
import django_filters

from orders_app.models import Order
from .models import Company, Invoice


class CompanyCreateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        exclude = ('added_at','')

class CompanyUpdateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        exclude = ('added_at','supplier_eik','supplier_dds','supplier_name','supplier_address','supplier_mol','supplier_phone_number','supplier_email')

class InvoiceCreateForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'
        exclude = ['date', 'cancelled']

class InvoiceUpdateForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'
        exclude = ['date']

class InvoiceReportFilter(django_filters.FilterSet):
    whole_price_without_dds = django_filters.RangeFilter(
        widget=django_filters.widgets.RangeWidget(
            attrs={'placeholder': 'Price without VAT'}))

    whole_price_with_dds = django_filters.RangeFilter(
        widget=django_filters.widgets.RangeWidget(
            attrs={'placeholder': 'Price with VAT'}))

    date = django_filters.DateFromToRangeFilter(
        widget=django_filters.widgets.RangeWidget(
            attrs={'type': 'date'}))

    DDS = django_filters.ChoiceFilter(
        label="DDS",
        choices=lambda: [(d, d) for d in Invoice.objects.values_list("DDS", flat=True).distinct()],
        widget=forms.Select(attrs={
            'class': 'select2',
            'data-placeholder': 'VAT'
        })
    )

    cancelled = django_filters.ChoiceFilter(
        choices=[
            ('', 'Status'),
            ('False', 'Active'),
            ('True', 'Cancelled'),
        ],
        empty_label=None)

    company = django_filters.ModelChoiceFilter(
        queryset=Company.objects.all(),
        widget=forms.Select(attrs={
            'class': 'select2',
            'data-placeholder': 'Company'
        }))

    order = django_filters.ModelChoiceFilter(
        queryset=Order.objects.all(),
        widget=forms.Select(attrs={
            'class': 'select2',
            'data-placeholder': 'Order'
        })
    )

    class Meta:
        model = Invoice
        fields = {'DDS',
                  'cancelled',
                  'company',
                  'order',}