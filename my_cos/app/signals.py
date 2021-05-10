from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Product
from .handlers_service import get_ingredients_names_list_from_string
from .services import add_ingredients_in_product


@receiver(post_save, sender=Product)
def add_new_ingredients(sender, instance, **kwargs):
    """When creating or updating the product, the product.ingredients field value
    split by the names, and adding the ingredients with this names to the product
    ingredients list"""
    if instance.ingredients and instance.approved:
        ingredients_names = get_ingredients_names_list_from_string(
            ingredients=instance.ingredients
        )
        add_ingredients_in_product(
            names=ingredients_names,
            instance=instance
        )
        Product.objects.filter(id=instance.id).update(ingredients='')
