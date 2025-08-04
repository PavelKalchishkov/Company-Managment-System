from django import forms

from .models import Client

class ClientCreateForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'company': forms.Select(attrs={'class': 'select2'})
        }
        exclude = ('added_at',)

class ClientUpdateForm(forms.ModelForm):
    class Meta:
        model = Client
        fields = '__all__'
        widgets = {
            'company': forms.Select(attrs={'class': 'select2'})
        }
        exclude = ('added_at',)