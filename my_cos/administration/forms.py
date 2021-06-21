from django import forms
from django.utils.translation import gettext_lazy as _

from app.models import Product, Ingredient


class ProductAdminForm(forms.ModelForm):
    brand = forms.CharField(
        max_length=100,
        required=True,
        widget=forms.TextInput(
            attrs={
                'class': 'form-general form-input',
                'placeholder': _('Enter brand name')
            }
        )
    )
    ingredients_list = forms.ModelMultipleChoiceField(
        required=False,
        queryset=Ingredient.objects.all().order_by('name'),
        widget=forms.SelectMultiple(
            attrs={
                'class': 'form-general form-choice'
            }
        )
    )

    class Meta:
        model = Product
        fields = [
            'brand',
            'line',
            'name',
            'country',
            'img',
            'ingredients',
            'ingredients_list',
            'ph',
            'effect_type',
            'skin_type',
            'for_what',
            'ebay_link',
            'amazon_link',
            'blog_link',
            'youtube_link',
            'facebook_link',
            'telegram_link',
            'instagram_link',
            'approved',
        ]
        widgets = {
            'line': forms.TextInput(
                attrs={
                    'class': 'form-general form-input',
                    'placeholder': _('Enter brand line'),
                    'required': False
                }),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-general form-input',
                    'placeholder': _('Enter product name'),
                    'required': True
                }),
            'country': forms.Select(
                attrs={
                    'class': 'form-general form-input',
                    'required': False,
                }),
            'ingredients': forms.Textarea(
                attrs={
                    'class': 'form-general form-textarea',
                    'placeholder': _('Enter ingredients...'),
                    'required': False
                }),
            'ph': forms.Select(
                attrs={
                    'class': 'form-general form-choice',
                    'required': False
                }),
            'ebay_link': forms.TextInput(
                attrs={
                    'class': 'form-general form-link',
                    'placeholder': _('enter ebay link'),
                    'required': False
                }),
            'amazon_link': forms.TextInput(
                attrs={
                    'class': 'form-general form-link',
                    'placeholder': _('enter amazon link'),
                    'required': False
                }),
            'blog_link': forms.TextInput(
                attrs={
                    'class': 'form-general form-link',
                    'placeholder': _('enter blog link'),
                    'required': False
                }),
            'youtube_link': forms.TextInput(
                attrs={
                    'class': 'form-general form-link',
                    'placeholder': _('enter youtube link'),
                    'required': False
                }),
            'facebook_link': forms.TextInput(
                attrs={
                    'class': 'form-general form-link',
                    'placeholder': _('enter facebook link'),
                    'required': False
                }),
            'telegram_link': forms.TextInput(
                attrs={
                    'class': 'form-general form-link',
                    'placeholder': _('enter telegram link'),
                    'required': False
                }),
            'instagram_link': forms.TextInput(
                attrs={
                    'class': 'form-general form-link',
                    'placeholder': _('enter instagram link'),
                    'required': False
                }),
        }
