from modeltranslation.translator import register, TranslationOptions

from app.models import Ingredient, Product, Country


@register(Ingredient)
class IngredientTranslationOptions(TranslationOptions):
    pass


@register(Product)
class ProductTranslationOptions(TranslationOptions):
    pass


@register(Country)
class CountryTranslationOptions(TranslationOptions):
    pass