from .models import Ingredient


def add_ingredients_in_product(names: list[str], instance) -> None:
    """Get list of the ingredients names, get or create ingredient with this name
    and add it to the product ingredient list."""
    ingredients_qs = Ingredient.objects.all()

    for name in names:
        try:
            ingredient = ingredients_qs.get(name=name)
            instance.ingredients_list.add(ingredient)
        except Ingredient.DoesNotExist:
            ingredient = Ingredient(name=name)
            ingredient.save()
            instance.ingredients_list.add(ingredient)


