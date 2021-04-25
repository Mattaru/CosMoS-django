from django import forms

from app.models import Brand, Country,  Product


class BrandForm(forms.ModelForm):

    class Meta:
        model = Brand
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-general form-input',
                    'placeholder': 'Write brand name here',
                    'required': True,
                }),
            'country': forms.Select(
                attrs={
                    'class': 'form-general form-input',
                    'required': True,
                }),
            'description': forms.Textarea(
                attrs={
                    'class': 'form-general form-textarea',
                    'placeholder': 'Write info about the brand here...',
                    'required': False,
                })
        }


class CountryForm(forms.ModelForm):

    class Meta:
        model = Country
        fields = ['name']
        widgets = {
            'name': forms.TextInput(
                attrs={
                    'class': 'form-general form-input',
                    'placeholder': 'Write country name here',
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
            'brand': forms.Select(
                attrs={
                    'class': 'form-general form-input',
                    'required': True,
                }),
            'line': forms.TextInput(
                attrs={
                    'class': 'form-general form-input',
                    'placeholder': 'Write brand line here',
                    'required': False,
                }),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-general form-input',
                    'placeholder': 'Write product name here',
                    'required': True,
                }),
            'ingredients': forms.Textarea(
                attrs={
                    'class': 'form-general form-textarea',
                    'placeholder': 'Write ingredients here...',
                    'required': True,
                }),
            'ph': forms.Select(
                attrs={
                    'class': 'form-general form-input',
                    'placeholder': 'Write product name here',
                    'required': False,
                }),
        }


class OneRowSearch(forms.Form):
    search = forms.CharField(max_length=255, label='', widget=forms.TextInput(
        attrs={
            'class': 'search-form-input',
            'placeholder': 'brand | line | product',
        }
    ), required=False)
