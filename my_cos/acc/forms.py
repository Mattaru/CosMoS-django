from django import forms

from app.models import Product


class ProductAdminForm(forms.Form):
    name = forms.CharField(widget=forms.CharField(max_length=200, validators=[]))

    class Meta:
        model = Product
        fields = [
            'brand',
            'line',
            'name',
            'img',
            'ingredients',
            'ingredients_img',
            'ph',
            'effect_type',
            'skin_type',
            'for_what',
            'ebay_link',
            'blog_link',
            'youtube_link',
            'approved',
        ]