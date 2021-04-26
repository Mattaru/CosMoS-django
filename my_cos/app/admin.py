from django.contrib import admin

from app.models import Country, Product


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
