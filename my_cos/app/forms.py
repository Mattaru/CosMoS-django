from django import forms
from django.utils.translation import gettext_lazy as _

from app.models import Country, Product


class CountryForm(forms.ModelForm):

    class Meta:
        model = Country
        fields = ['name']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-general form-input',
                    'max_length': '10',
                    'required': True,
                })
        }


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = [
            'brand',
            'line',
            'name',
            'ingredients',
            'ph',
            'effect_type',
            'skin_type',
            'for_what',
        ]
        widgets = {
            'brand': forms.TextInput(
                attrs={
                    'class': 'form-general form-input',
                    'placeholder': _('Write brand here'),
                    'required': True,
                }),
            'line': forms.TextInput(
                attrs={
                    'class': 'form-general form-input',
                    'placeholder': _('Write brand line here'),
                    'required': False,
                }),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-general form-input',
                    'placeholder': _('Write product name here'),
                    'required': True,
                }),
            'ingredients': forms.Textarea(
                attrs={
                    'class': 'form-general form-textarea',
                    'placeholder': _('Write ingredients here...'),
                    'required': False,
                }),
            'ph': forms.Select(
                attrs={
                    'class': 'form-general form-input',
                    'placeholder': _('Write product name here'),
                    'required': False,
                }),
        }


class OneRowSearch(forms.Form):
    search = forms.CharField(max_length=255, label='', widget=forms.TextInput(
        attrs={
            'class': 'search-form-input',
            'placeholder': _('brand | line | product'),
        }
    ), required=False)
