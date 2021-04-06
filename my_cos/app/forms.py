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
    brand = forms.ModelChoiceField(queryset=Brand.objects.all(), required=True)
    name = forms.CharField(max_length=200, required=True)
    ingredients = forms.CharField(widget=forms.Textarea(), required=True)

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
