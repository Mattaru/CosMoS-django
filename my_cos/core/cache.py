from django.core.cache import cache


def set_product_cache(instance, model):
    """Set cache when product created or saved"""
    cache.set(
        'approved_product_list',
        model.objects.filter(approved=True).select_related('country').order_by('name')
    )
    cache.set(
        'unapproved_product_list',
        model.objects.filter(approved=False).select_related('country').order_by('name')
    )
    cache.set(
        'main_page_queryset',
        model.objects.filter(approved=True).order_by('-creation_date')[:9]
    )
