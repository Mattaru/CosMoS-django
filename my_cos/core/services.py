from app.models import Ingredient
from django.db import IntegrityError


def add_ingredients_in_product(names: list[str], instance) -> None:
    """Get list of the ingredients names, get or create ingredient with this name
    and add it to the product ingredient list."""
    print(names)
    for name in names:

        if Ingredient.objects.filter(name__iexact=name).exists():
            try:
                ingredient = Ingredient.objects.get(name__iexact=name)
            except Ingredient.DoesNotExist:
                ingredient = Ingredient(name=name)
                ingredient.save()

        else:
            ingredient = Ingredient(name=name)
            ingredient.save()

        ingredient.product_set.add(instance)
