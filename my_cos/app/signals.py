from django.db.models.signals import post_save
from django.dispatch import receiver

from app.models import (Product, Ingredient)


def ingredients_names_handler(text):
    """

    """
    names_list = text.split(',')
    ingredients_names = []

    for name in names_list:
        ingredient_name = name.split(' ')
        new_name = []

        for word in ingredient_name:
            new_word = word.strip(' ').capitalize()
            new_name.append(new_word)

        new_name = ' '.join(new_name)
        ingredients_names.append(new_name)

    return ingredients_names


@receiver(post_save, sender=Product)
def add_new_ingredients(sender, instance, **kwargs):
    if instance.ingredients and instance.approved:
        ingredients_names = ingredients_names_handler(instance.ingredients)
        ingredients_qs = Ingredient.objects.all()

        for name in ingredients_names:
            try:
                ingredient = ingredients_qs.get(name=name)
                instance.ingredients_list.add(ingredient)
            except Ingredient.DoesNotExist:
                ingredient = Ingredient(name=name)
                ingredient.save()
                instance.ingredients_list.add(ingredient)

        Product.objects.filter(id=instance.id).update(ingredients='')
