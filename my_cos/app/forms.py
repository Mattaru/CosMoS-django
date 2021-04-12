from django import forms

from app.models import Brand, Country,  Product


input_style = 'width: 40%;'\
              'padding: 10px;'\
              'border-radius: 5px;'\
              'text-align: center;'\
              'border: 1px solid rgba(98, 129, 164);'

textarea_style = 'width: 80%;'\
                'padding: 10px;'\
                'border-radius: 5px;'\
                'border: 1px solid rgba(98, 129, 164);'


class BrandForm(forms.ModelForm):
    class Meta:
        model = Brand
        fields = '__all__'


class CountryForm(forms.ModelForm):
    class Meta:
        model = Country
        fields = ['name']


class ProductForm(forms.ModelForm):
    brand = forms.ModelChoiceField(queryset=Brand.objects.all(), widget=forms.Select(
        attrs={
            'style': input_style,
            'placeholder': 'Write brand name here'
        }
    ), required=True)
    line = forms.CharField(max_length=100, widget=forms.TextInput(
        attrs={
            'style': input_style,
            'placeholder': 'Write brand line here'
        }
    ))
    name = forms.CharField(max_length=200,widget=forms.TextInput(
        attrs={
            'style': input_style,
            'placeholder': 'Write product name here'
        }
    ), required=True)
    ingredients = forms.CharField(widget=forms.Textarea(
        attrs={
            'style': textarea_style,
            'placeholder': 'Write ingredients here...'
        }
    ), required=True)
    ph = forms.ChoiceField(choices=Product.NumberPH.choices, widget=forms.Select(
        attrs={
            'style': input_style,
            'placeholder': 'Write product name here'
        }
    ), required=False)

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
