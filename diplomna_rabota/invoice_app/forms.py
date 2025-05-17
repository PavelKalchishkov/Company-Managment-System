from django import forms

from .models import Company


class CompanyCreateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'

class CompanyUpdateForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = '__all__'