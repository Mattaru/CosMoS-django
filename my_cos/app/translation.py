from modeltranslation.translator import register, TranslationOptions

from app.models import Product, Country


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    pass


@register(Country)
class CountryTranslationOptions(TranslationOptions):
    pass