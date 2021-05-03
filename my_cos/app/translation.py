from modeltranslation.translator import register, TranslationOptions

from app.models import Product, Country


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    fields = (
        'country',
        'ingredients',
        'ph',
        'effect_type',
        'skin_type',
        'for_what',
    )


@register(Country)
class CountryTranslationOptions(TranslationOptions):
    fields = (
        'name',
    )