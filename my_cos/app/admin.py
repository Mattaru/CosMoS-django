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
    search_fields = ('name',)


@admin.register(Country)
class CountryAdmin(TranslationAdmin):
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name',)


@admin.register(Product)
class ProductAdmin(TranslationAdmin):
    list_display = (
        'name',
        'brand',
        'line',
        'created_by',
        'approved',
    )
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ('name', 'brand', 'line')
