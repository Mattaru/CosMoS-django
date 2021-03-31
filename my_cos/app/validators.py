from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

from app import models


def unique_product_name(value):
    """
    Take a value from the form field and check he's unique in the DB.
    """
    if models.Product.objects.filter(name__icontains=value):
        raise ValidationError(
            _('Name %(value)s already exist.'),
            params={'value': value}
        )


def unique_country_name(value):
    """
    Take a value from the form field and check he's unique in the DB.
    """
    if models.Country.objects.filter(name__icontains=value):
        raise ValidationError(
            _('Name %(value)s already exist.'),
            params={'value': value}
        )


def unique_brand_name(value):
    """
    Take a value from the form field and check he's unique in the DB.
    """
    if models.Brand.objects.filter(name__icontains=value):
        raise ValidationError(
            _('Name %(value)s already exist.'),
            params={'value': value}
        )