from app.models import Ingredient
from django.db import IntegrityError


def add_ingredients_in_product(names: list[str], instance) -> None:
    """Get list of the ingredients names, get or create ingredient with this name
    and add it to the product ingredient list."""
    for name in names:
        try:
            ingredient = Ingredient.objects.get(name=name)
        except Ingredient.DoesNotExist:
            ingredient = Ingredient(name=name)
            ingredient.save()

        ingredient.product_set.add(instance)
