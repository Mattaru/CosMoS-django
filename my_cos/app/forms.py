from django import forms

from app.models import Brand, Country,  Product


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['name']


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


class OneRowSearch(forms.Form):
    search = forms.CharField(max_length=255, required=False, label='',
                             widget=forms.TextInput(attrs={'placeholder': 'brand | line | product'}))
