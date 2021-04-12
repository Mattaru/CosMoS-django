from django.db.models import Q
from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.core.exceptions import ValidationError
from django.core.exceptions import NON_FIELD_ERRORS

from multiselectfield import MultiSelectField


class Country(models.Model):
    name = models.CharField(_('country name'), max_length=100, unique=True)
    flag_img_name = models.CharField(_('flag image name'), max_length=50,
                                     blank=True, null=True)

    def __str__(self):
        return self.name

    def make_flag_image_name(self):
        self.flag_img_name = f"{'-'.join(self.name.split(' ')).lower()}.svg"

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if self.name:
            self.make_flag_image_name()
            return super().save(*args, **kwargs)

    def validate_unique(self, *args, **kwargs):
        qs = Country.objects.filter(~Q(id=self.id))
        if qs.filter(name__icontains=self.name).exists():
            raise ValidationError(_("Item with the same name is already exists."))
        super(Country, self).validate_unique(*args, **kwargs)


class Brand(models.Model):
    name = models.CharField(_('brand name'), max_length=100, unique=True)
    description = models.TextField(_('description'), blank=True, null=True)
    country = models.ForeignKey('app.Country', verbose_name=_('Country'), null=True, blank=True,
                                on_delete=models.SET_NULL, related_name='brand_country')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('app:brand_detail', args=[self.id])

    def validate_unique(self, *args, **kwargs):
        qs = Brand.objects.filter(~Q(id=self.id))
        if qs.filter(name__icontains=self.name).exists():
            raise ValidationError(_("Item with the same name is already exists."))
        super(Brand, self).validate_unique(*args, **kwargs)


class Product(models.Model):
    brand = models.ForeignKey('app.Brand', verbose_name=_('brand'), null=True, blank=True,
                                   on_delete=models.SET_NULL, related_name='product_brand')
    line = models.CharField(_('line'), max_length=100, blank=True, null=True)
    name = models.CharField(_('product name'), max_length=200, unique=True)
    img = models.ImageField(_('image'), upload_to='product_img/', default='unknown.png', )
    ingredients = models.TextField(_('ingredients'))
    ingredients_img = models.ImageField(_('ingredients image'), upload_to='product_img/consistency/',
                                        blank=True, null=True)

    class NumberPH(models.TextChoices):
        FORE = '4', _('4')
        FORE_HALF = '4.5', _('4.5')
        FIVE = '5', _('5')
        FIVE_HALF = '5.5', _('5.5')
        SIX = '6', _('6')
        SIX_HALF = '6.5', _('6.5')
        SEVEN = '7', _('7')
        SEVEN_HALF = '7.5', _('7.5')
        EIGHT = '8', _('8')
        EIGHT_HALF = '8.5', _('8.5')
        NINE = '9', _('9')

        __empty__ = _('Absent')

    ph = models.CharField(_('ph'), choices=NumberPH.choices, max_length=3,
                          null=True, blank=True)

    class EffectType(models.TextChoices):
        CALMING = 'calming', _('Calming')
        ANTI_WRINKLE = 'anti wrinkle', _('Anti wrinkle')
        ELASTICITY = 'skin elasticity', _('Skin elasticity')
        MOISTURIZING = 'moisturizing', _('Moisturizing')
        MICROBIOME = 'skin microbiome', _('Skin microbiome')
        SUN_PROTECTION = 'sun protection', _('Sun protection')
        LIFTING = 'lifting', _('Lifting')
        HEALING = 'healing', _('Healing')
        ANTIPIGMENTATION = 'antipigmentation', _('Antipigmentation')

    effect_type = MultiSelectField(_('effect type'), choices=EffectType.choices, max_length=113,
                                   null=True, blank=True)

    class SkinType(models.TextChoices):
        NORMAL = 'normal', _('Normal')
        OILY = 'oily', _('Oily')
        DRY = 'dry', _('Dry')
        DEHYDRATED = 'dehydrated', _('Dehydrated')
        AGING = 'aging', _('Aging')
        TEENAGE = 'teenage', _('Teenage')
        BABY = 'baby', _('Baby')
        PROBLEM = 'problem', _('Problem')
        COMBINATION = 'combination', _('Combination')
        FOR_ALL = 'all', _('All')

    skin_type = MultiSelectField(_('skin type'), choices=SkinType.choices, max_length=69,
                                 null=True, blank=True)

    class ForWhat(models.TextChoices):
        FC = 'face', _('Face')
        EY = 'eyes', _('Eyes')
        NK = 'neck', _('Neck')
        BD = 'body', _('Body')
        HR = 'hair', _('Hair')

    for_what = MultiSelectField(_('for what'), choices=ForWhat.choices, max_length=24,
                                null=True, blank=True)
    ebay_link = models.CharField(_('ebay(link)'), max_length=3000, blank=True, null=True)
    blog_link = models.CharField(_('blog(link)'), max_length=3000,
                                 blank=True, default='https://beauty-granny.com')
    youtube_link = models.CharField(_('youtube(link)'), max_length=3000, blank=True, null=True)
    approved = models.BooleanField(_('approved'), default=False)

    def __str__(self):
        return f'{self.name} -- {self.brand}'

    def get_absolute_url(self):
        return reverse('app:product_detail', args=[self.id])

    def validate_unique(self, *args, **kwargs):
        qs = Product.objects.filter(~Q(id=self.id))
        if qs.filter(name__icontains=self.name).exists():
            raise ValidationError(_("Item with the same name is already exists."))
        super(Product, self).validate_unique(*args, **kwargs)
