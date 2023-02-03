from django import forms

from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = '__all__'
        widgets = {
            'bouquet': forms.Select(
                attrs={'class': 'form-select'}
            ),
            'manager': forms.Select(
                attrs={'class': 'form-select'}
            ),
            'courier': forms.Select(
                attrs={'class': 'form-select'}
            ),
            'client': forms.Select(
                attrs={'class': 'form-select'}
            ),
            'address': forms.TextInput(
                attrs={'class': 'form-control'}
            ),
            'status': forms.Select(
                attrs={'class': 'form-select'}
            ),
            'delivery_time': forms.Select(
                attrs={'class': 'form-select'}
            ),
        }
