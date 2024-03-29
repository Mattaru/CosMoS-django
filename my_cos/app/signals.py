from django.db.models.signals import post_delete, post_save
from django.dispatch import receiver
from core.cache import set_product_cache

from core.decorators import on_transaction_commit
from core.handlers import get_ingredients_names_list_from_string
from core.services import add_ingredients_in_product
from .models import Product


@receiver(post_save, sender=Product)
@on_transaction_commit
def add_new_ingredients(sender, instance, **kwargs):
    """When creating or updating the product, the product.ingredients field value
    split by the names, and adding the ingredients with this names to the product
    ingredients list.'"""
    if instance.approved:
        set_product_cache(instance, sender)

    if instance.ingredients and instance.approved:
        ingredients_names = get_ingredients_names_list_from_string(
            ingredients=instance.ingredients
        )
        add_ingredients_in_product(
            names=ingredients_names,
            instance=instance
        )
        sender.objects.filter(id=instance.id).update(ingredients='')


@receiver(post_delete, sender=Product)
def cache_refresh_post_delete(sender, instance, **kwargs):
    """Refreshing cache after product delete."""
    set_product_cache(instance, sender)
