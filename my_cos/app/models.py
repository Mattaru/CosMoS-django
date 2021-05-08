import uuid

from django.db.models import Q
from django.db import models
from django.template.defaultfilters import slugify
from django.utils.translation import gettext_lazy as _
from django.urls import reverse
from django.core.exceptions import ValidationError

from multiselectfield import MultiSelectField


def get_img_upload_path(instance, filename):
    """
        Make new path for a files uploading.
    """
    return f'product-images/{instance.name}/{filename}'


class Country(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_('country name'), max_length=100, unique=True)
    slug = models.SlugField(max_length=100, null=True, unique=True)
    flag_img_name = models.CharField('flag image name', max_length=50,
                                     blank=True, null=True)

    class Meta:
        verbose_name = _('Country')
        verbose_name_plural = _('Countries')
        ordering = ['name']

    def __str__(self):
        return self.name

    def make_flag_image_name(self):
        self.flag_img_name = f"{'-'.join(self.name.split(' ')).lower()}.svg"

    def make_name_format(self):
        name = list(self.name.lower())
        name[0] = name[0].upper()
        self.name = ''.join(name)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if self.name:
            self.make_name_format()
            self.make_flag_image_name()

        if not self.slug and self.name:
            self.slug = slugify(self.name)

        return super().save(*args, **kwargs)

    def validate_unique(self, *args, **kwargs):
        qs = Country.objects.filter(~Q(id=self.id))
        if qs.filter(name__iexact=self.name).exists():
            raise ValidationError(_("Item with the same name is already exists."))
        super(Country, self).validate_unique(*args, **kwargs)

    def get_absolute_url(self):
        reverse('', kwargs={
            'slug': self.slug
        })


class Ingredient(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(_('ingredient name'), max_length=200, unique=True)
    slug = models.SlugField(max_length=200, null=True, unique=True)
    description = models.TextField()

    class SafetyClassification(models.TextChoices):
        SAFE = 'safe', _('Safe')
        NEUTRAL = 'neutral', _('Neutral')
        HARMFUL = 'harmful', _('Harmful')

        __empty__ = _('Absent')

    safety_classification = models.CharField(_('safety classification'), max_length=7,
                                             choices=SafetyClassification.choices, null=True, blank=True)
    creation_date = models.DateTimeField(_('date'), auto_now_add=True)
    approved = models.BooleanField(_('approved'), default=False)

    class Meta:
        verbose_name = _('Ingredient')
        verbose_name_plural = _('Ingredients')

    def __str__(self):
        return f'{self.name} -- ({self.description})'

    def validate_unique(self, *args, **kwargs):
        qs = Country.objects.filter(~Q(id=self.id))
        if qs.filter(name__iexact=self.name).exists():
            raise ValidationError(_("Item with the same name is already exists."))
        super(Ingredient, self).validate_unique(*args, **kwargs)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug and self.name:
            self.slug = slugify(self.name)

        return super().save(*args, **kwargs)


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    brand = models.CharField(_('brand'), max_length=100, blank=True, null=True)
    line = models.CharField(_('line'), max_length=100, blank=True, null=True)
    name = models.CharField(_('product name'), max_length=200, unique=True)
    slug = models.SlugField(max_length=200, null=True, unique=True)
    country = models.ForeignKey('app.Country', verbose_name=_('country'), blank=True, null=True,
                                on_delete=models.SET_NULL, related_name='Product_country')
    img = models.ImageField(_('image'), upload_to=get_img_upload_path, default='unknown.png', )
    ingredients = models.TextField(_('ingredients'))
    ingredients_list = models.ManyToManyField(Ingredient, blank=True)

    class NumberPH(models.TextChoices):
        FORE = '4', '4'
        FORE_HALF = '4.5', '4.5'
        FIVE = '5', '5'
        FIVE_HALF = '5.5', '5.5'
        SIX = '6', '6'
        SIX_HALF = '6.5', '6.5'
        SEVEN = '7', '7'
        SEVEN_HALF = '7.5', '7.5'
        EIGHT = '8', '8'
        EIGHT_HALF = '8.5', '8.5'
        NINE = '9', '9'

        __empty__ = _('Absent')

    ph = models.CharField('ph', choices=NumberPH.choices, max_length=3,
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
    ebay_link = models.CharField('ebay(link)', max_length=3000, blank=True, null=True)
    amazon_link = models.CharField('amazon(link)', max_length=3000, blank=True, null=True)
    blog_link = models.CharField('blog(link)', max_length=3000,
                                 blank=True, default='https://beauty-granny.com')
    youtube_link = models.CharField('youtube(link)', max_length=3000, blank=True, null=True)
    facebook_link = models.CharField('facebook(link)', max_length=3000, blank=True, null=True)
    telegram_link = models.CharField('telegram(link)', max_length=3000, blank=True, null=True)
    instagram_link = models.CharField('instagram(link)', max_length=3000, blank=True, null=True)
    creation_date = models.DateTimeField(_('date'), auto_now_add=True)
    approved = models.BooleanField(_('approved'), default=False)

    class Meta:
        verbose_name = _('Product')
        verbose_name_plural = _('Products')
        ordering = ['name', '-creation_date']

    def __str__(self):
        return f'{self.name} -- {self.brand}'

    def get_absolute_url(self):
        return reverse('app:product_detail', kwargs={
            'slug': self.slug
        })

    def validate_unique(self, *args, **kwargs):
        qs = Product.objects.filter(~Q(id=self.id))
        if qs.filter(name__iexact=self.name).exists():
            raise ValidationError(_("Item with the same name is already exists."))
        super(Product, self).validate_unique(*args, **kwargs)

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        if not self.slug and self.name:
            self.slug = slugify(self.name)

        return super().save(*args, **kwargs)
