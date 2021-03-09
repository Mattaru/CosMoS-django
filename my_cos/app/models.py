from django.db import models
from django.utils.translation import gettext_lazy as _

from multiselectfield import MultiSelectField


class Country(models.Model):
    name = models.CharField(verbose_name='Country name', max_length=100)
    flag_img = models.ImageField(verbose_name='Image', upload_to='flag_img/', default='unknown.png')

    def __str__(self):
        return self.name


class Brend(models.Model):
    name = models.CharField(verbose_name='Brand name', max_length=100)
    country = models.ForeignKey('app.Country', verbose_name='Country', null=True, blank=True,
                                on_delete=models.SET_NULL, related_name='brend_country')

    def __str__(self):
        return f'{self.name}({self.country})'


class Product(models.Model):
    brend = models.ForeignKey('app.Brend', verbose_name='Brend', null=True, blank=True,
                              on_delete=models.SET_NULL, related_name='product_brend')
    name = models.CharField(verbose_name='Product name', max_length=200)
    img = models.ImageField(verbose_name='Image', upload_to='product_img/', default='unknown.png')
    consistency = models.TextField(verbose_name='Consistency')

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

    ph = models.CharField(verbose_name='pH', choices=NumberPH.choices, max_length=3, null=True, blank=True)

    class EffectType(models.TextChoices):
        CALMING = 'calming', 'Calming'
        ANTI_WRINKLE = 'anti wrinkle', 'Anti wrinkle'
        ELASTICITY = 'skin elasticity', 'Skin elasticity'
        MOISTURIZING = 'moisturizing', 'Moisturizing'
        MICROBIOME = 'skin microbiome', 'Skin microbiome'
        SUN_PROTECTION = 'sun protection', 'Sun protection'
        LIFTING = 'lifting', 'Lifting'
        HEALING = 'healing', 'Healing'
        ANTIPIGMENTATION = 'antipigmentation', 'Antipigmentation'

    effect_type = MultiSelectField(verbose_name='Effect type', choices=EffectType.choices, max_length=113, null=True, blank=True)

    class SkinType(models.TextChoices):
        NORMAL = 'normal', 'Normal'
        OILY = 'oily', 'Oily'
        DRY = 'dry', 'Dry'
        DEHYDRATED = 'dehydrated', 'Dehydrated'
        AGING = 'aging', 'Aging'
        TEENAGE = 'teenage', 'Teenage'
        BABY = 'baby', 'Baby'
        PROBLEM = 'problem', 'Problem'
        COMBINATION = 'combination', 'Combination'
        FOR_ALL = 'all', 'All'

    skin_type = MultiSelectField(verbose_name='Skin type', choices=SkinType.choices, max_length=69, null=True, blank=True)

    class ForWhat(models.TextChoices):
        FC = 'face', 'Face'
        EY = 'eyes', 'Eyes'
        NK = 'neck', 'Neck'
        BD = 'body', 'Body'
        HR = 'hair', 'Hair'

    for_what = MultiSelectField(verbose_name='For what', choices=ForWhat.choices, max_length=24, null=True, blank=True)
    ebay_link = models.CharField(verbose_name='Ebay(link)', max_length=3000)
    blog_link = models.CharField(verbose_name='Blog(link)', max_length=3000)
    youtube_link = models.CharField(verbose_name='Youtube(link)', max_length=3000)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} -- {self.brend}'

