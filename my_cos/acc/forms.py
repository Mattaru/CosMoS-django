from django import forms

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
            'ingredients_img',
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
                    'placeholder': 'Write brand line here',
                    'required': True
                }),
            'line': forms.TextInput(
                attrs={
                    'class': 'form-general form-input',
                    'placeholder': 'Write brand line here',
                    'required': False
                }),
            'name': forms.TextInput(
                attrs={
                    'class': 'form-general form-input',
                    'placeholder': 'Write product name here',
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
                    'placeholder': 'Write ingredients here...',
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
                    'placeholder': 'ebay link here',
                    'required': False
                }),
            'amazon_link': forms.TextInput(
                attrs={
                    'class': 'form-general form-link',
                    'placeholder': 'amazon link here',
                    'required': False
                }),
            'blog_link': forms.TextInput(
                attrs={
                    'class': 'form-general form-link',
                    'placeholder': 'blog link here',
                    'required': False
                }),
            'youtube_link': forms.TextInput(
                attrs={
                    'class': 'form-general form-link',
                    'placeholder': 'youtube link here',
                    'required': False
                }),
            'facebook_link': forms.TextInput(
                attrs={
                    'class': 'form-general form-link',
                    'placeholder': 'facebook link here',
                    'required': False
                }),
            'telegram_link': forms.TextInput(
                attrs={
                    'class': 'form-general form-link',
                    'placeholder': 'telegram link here',
                    'required': False
                }),
            'instagram_link': forms.TextInput(
                attrs={
                    'class': 'form-general form-link',
                    'placeholder': 'instagram link here',
                    'required': False
                }),
        }
