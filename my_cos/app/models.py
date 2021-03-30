from django.db import models
from django.utils.translation import gettext_lazy as _
from django.urls import reverse

from multiselectfield import MultiSelectField


class Country(models.Model):
    name = models.CharField(verbose_name='Country name', max_length=100, unique=True)
    flag_img_name = models.CharField(verbose_name='Flag image name', max_length=50,
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


class Brand(models.Model):
    name = models.CharField(verbose_name='Brand name', max_length=100, unique=True)
    description = models.TextField(verbose_name='Description', blank=True, null=True)
    country = models.ForeignKey('app.Country', verbose_name='Country', null=True, blank=True,
                                on_delete=models.SET_NULL, related_name='brand_country')

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('app:brand_detail', args=[self.id])


class Product(models.Model):
    brand = models.ForeignKey('app.Brand', verbose_name='Brand', null=True, blank=True,
                                   on_delete=models.SET_NULL, related_name='product_brand')
    line = models.CharField(verbose_name='line', max_length=100, blank=True, null=True)
    name = models.CharField(verbose_name='Product name', max_length=200, unique=True)
    img = models.ImageField(verbose_name='Image', upload_to='product_img/', default='unknown.png', )
    ingredients = models.TextField(verbose_name='Ingredients')
    ingredients_img = models.ImageField(verbose_name='Ingredients image', upload_to='product_img/consistency/',
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

    ph = models.CharField(verbose_name='pH', choices=NumberPH.choices, max_length=3,
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

    effect_type = MultiSelectField(verbose_name='Effect type', choices=EffectType.choices, max_length=113,
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

    skin_type = MultiSelectField(verbose_name='Skin type', choices=SkinType.choices, max_length=69,
                                 null=True, blank=True)

    class ForWhat(models.TextChoices):
        FC = 'face', _('Face')
        EY = 'eyes', _('Eyes')
        NK = 'neck', _('Neck')
        BD = 'body', _('Body')
        HR = 'hair', _('Hair')

    for_what = MultiSelectField(verbose_name='For what', choices=ForWhat.choices, max_length=24,
                                null=True, blank=True)
    ebay_link = models.CharField(verbose_name='Ebay(link)', max_length=3000, blank=True, null=True)
    blog_link = models.CharField(verbose_name='Blog(link)', max_length=3000,
                                 blank=True, default='https://beauty-granny.com')
    youtube_link = models.CharField(verbose_name='Youtube(link)', max_length=3000, blank=True, null=True)
    approved = models.BooleanField(default=False)

    def __str__(self):
        return f'{self.name} -- {self.brand}'

    def get_absolute_url(self):
        return reverse('app:product_detail', args=[self.id])



