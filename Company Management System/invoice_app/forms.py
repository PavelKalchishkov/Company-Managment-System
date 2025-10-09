from django import forms
import django_filters
from django.utils.translation import gettext_lazy as _

from orders_app.models import Order
from .models import Company, Invoice


class CompanyCreateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        exclude = ('added_at',)

        labels = {
            'eik': _('eik'),
            'dds': _('dds'),
            'name': _('name'),
            'address': _('address'),
            'mol': _('mol'),
            'recipient': _('recipient'),
        }

class CompanyUpdateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        exclude = ('added_at','supplier_eik','supplier_dds','supplier_name','supplier_address','supplier_mol','supplier_phone_number','supplier_email')

        labels = {
            'eik': _('eik'),
            'dds': _('dds'),
            'name': _('name'),
            'address': _('address'),
            'mol': _('mol'),
            'recipient': _('recipient'),
        }

class InvoiceCreateForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'
        exclude = ['date', 'cancelled']

        labels = {
            'company': _('company'),
            'order': _('order'),
            'DDS': _('DDS'),
            'comment': _('comment'),
            'discount': _('discount'),
            'whole_price_with_dds': _('whole_price_with_dds'),
            'whole_price_without_dds': _('whole_price_without_dds'),
        }

class InvoiceUpdateForm(forms.ModelForm):
    class Meta:
        model = Invoice
        fields = '__all__'
        exclude = ['date']

    labels = {
        'company': _('company'),
        'order': _('order'),
        'DDS': _('DDS'),
        'comment': _('comment'),
        'discount': _('discount'),
        'whole_price_with_dds': _('whole_price_with_dds'),
        'whole_price_without_dds': _('whole_price_without_dds'),
    }

class InvoiceReportFilter(django_filters.FilterSet):
    whole_price_without_dds = django_filters.RangeFilter(
        widget=django_filters.widgets.RangeWidget(
            attrs={'placeholder': _('Price without VAT')}))

    whole_price_with_dds = django_filters.RangeFilter(
        widget=django_filters.widgets.RangeWidget(
            attrs={'placeholder': _('Price with VAT')}))

    date = django_filters.DateFromToRangeFilter(
        widget=django_filters.widgets.RangeWidget(
            attrs={'type': 'date'}))

    DDS = django_filters.ChoiceFilter(
        label="DDS",
        choices=lambda: [(d, d) for d in Invoice.objects.values_list("DDS", flat=True).distinct()],
        widget=forms.Select(attrs={
            'class': 'select2',
            'data-placeholder': _('VAT')
        })
    )

    cancelled = django_filters.ChoiceFilter(
        choices=[
            ('', _('Status')),
            ('False', _('Active')),
            ('True', _('Cancelled')),
        ],
        empty_label=None)

    company = django_filters.ModelChoiceFilter(
        queryset=Company.objects.all(),
        widget=forms.Select(attrs={
            'class': 'select2',
            'data-placeholder': _('Company')
        }))

    order = django_filters.ModelChoiceFilter(
        queryset=Order.objects.all(),
        widget=forms.Select(attrs={
            'class': 'select2',
            'data-placeholder': _('Order')
        })
    )

    class Meta:
        model = Invoice
        fields = {'DDS',
                  'cancelled',
                  'company',
                  'order',}