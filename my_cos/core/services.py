from django.db import IntegrityError

from app.models import Ingredient


def add_ingredients_in_product(names: list[str], instance) -> None:
    """Get list of the ingredients names, get or create ingredient with this name
    and add it to the product ingredients list."""
    list_of_ingredients = []

    for name in names:
        try:
            ingredient = Ingredient.objects.get(name__iexact=name)
        except Ingredient.DoesNotExist:
            ingredient = Ingredient(name=name)
            ingredient.save()

        list_of_ingredients.append(ingredient)

    instance.ingredients_list.add(*list_of_ingredients)
