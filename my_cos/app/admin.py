from django.contrib import admin

from app.models import Country, Brend, Product


@admin.register(Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(Brend)
class BrendAdmin(admin.ModelAdmin):
    pass


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    pass
