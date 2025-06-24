from django import forms
import django_filters
from .models import Company, Invoice


class CompanyCreateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        exclude = ('added_at',)

class CompanyUpdateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        exclude = ('added_at',)

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
    whole_price_without_dds = django_filters.RangeFilter()
    whole_price_with_dds = django_filters.RangeFilter()
    date = django_filters.DateFromToRangeFilter(
        widget=django_filters.widgets.RangeWidget(
            attrs={'type': 'date'}
        )
    )

    class Meta:
        model = Invoice
        fields = {'DDS',
                  'cancelled',
                  'company',
                  'order',}