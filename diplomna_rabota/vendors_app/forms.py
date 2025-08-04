from django import forms
from .models import Vendor


class VendorCreationForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'
        exclude = ('added_at',)

class VendorUpdateForm(forms.ModelForm):
    class Meta:
        model = Vendor
        fields = '__all__'
        exclude = ('added_at',)