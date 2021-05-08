from django.contrib import admin

from modeltranslation.admin import TranslationAdmin

from app.models import (Country, Ingredient, Product)


@admin.register(Ingredient)
class IngredientAdmin(TranslationAdmin):
    list_display = (
        'name',
        'description',
        'approved'
    )
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Country)
class CountryAdmin(TranslationAdmin):
    prepopulated_fields = {'slug': ('name',)}


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = (
        'brand',
        'line',
        'name',
        'approved',
    )
    prepopulated_fields = {'slug': ('name',)}
