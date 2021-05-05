from django import forms
from django.utils.translation import gettext_lazy as _

from app.models import Product


class ProductAdminForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = [
            'brand',
            'line',
            'name',
            'country',
            'img',
            'ingredients',
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
            'brand': forms.TextInput(
                attrs={
                    'class': 'form-general form-input',
                    'placeholder': _('Write brand line here'),
                    'required': True
                }),
            'line': forms.TextInput(
                attrs={
                    'class': 'form-general form-input',
                    'placeholder': _('Write brand line here'),
                    'required': False
                }),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-general form-input',
                    'placeholder': _('Write product name here'),
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
                    'placeholder': _('Write ingredients here...'),
                    'required': True
                }),
            'ph': forms.Select(
                attrs={
                    'class': 'form-general form-input',
                    'required': False
                }),
            'ebay_link': forms.TextInput(
                attrs={
                    'class': 'form-general form-link',
                    'placeholder': _('ebay link here'),
                    'required': False
                }),
            'amazon_link': forms.TextInput(
                attrs={
                    'class': 'form-general form-link',
                    'placeholder': _('amazon link here'),
                    'required': False
                }),
            'blog_link': forms.TextInput(
                attrs={
                    'class': 'form-general form-link',
                    'placeholder': _('blog link here'),
                    'required': False
                }),
            'youtube_link': forms.TextInput(
                attrs={
                    'class': 'form-general form-link',
                    'placeholder': _('youtube link here'),
                    'required': False
                }),
            'facebook_link': forms.TextInput(
                attrs={
                    'class': 'form-general form-link',
                    'placeholder': _('facebook link here'),
                    'required': False
                }),
            'telegram_link': forms.TextInput(
                attrs={
                    'class': 'form-general form-link',
                    'placeholder': _('telegram link here'),
                    'required': False
                }),
            'instagram_link': forms.TextInput(
                attrs={
                    'class': 'form-general form-link',
                    'placeholder': _('instagram link here'),
                    'required': False
                }),
        }
