from django import forms


class OneRowSearch(forms.Form):
    search = forms.CharField(max_length=255, required=False, label='',
                             widget=forms.TextInput(attrs={'placeholder': 'brand | line | product'}))
