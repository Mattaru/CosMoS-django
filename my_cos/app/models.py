from django.db import models

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
    CALMING = 'calming'
    ANTI_WRINKLE = 'anti wrinkle'
    ELASTICITY = 'skin elasticity'
    MOISTURIZING = 'moisturizing'
    MICROBIOME = 'skin microbiome'
    SUN_PROTECTION = 'sun protection'
    LIFTING = 'lifting'
    HEALING = 'healing'
    ANTIPIGMENTATION = 'antipigmentation'
    EFFECT_TYPE = (
        (CALMING, 'Calming'),
        (ANTI_WRINKLE, 'Anti wrinkle'),
        (ELASTICITY, 'Skin elasticity'),
        (MOISTURIZING, 'Moisturizing'),
        (MICROBIOME, 'Skin microbiome'),
        (SUN_PROTECTION, 'Sun protection'),
        (LIFTING, 'Lifting'),
        (HEALING, 'Healing'),
        (ANTIPIGMENTATION, 'Antipigmentation'),
    )
    effect_type = MultiSelectField(verbose_name='Effect type', choices=EFFECT_TYPE, max_length=113)
    NORMAL = 'normal'
    OILY = 'oily'
    DRY = 'dry'
    DEHYDRATED = 'dehydrated'
    AGING = 'aging'
    TEENAGE = 'teenage'
    BABY = 'baby'
    PROBLEM = 'problem'
    COMBINATION = 'combination'
    FOR_ALL = 'all'
    SKIN_TYPE = (
        (NORMAL, 'Normal'),
        (OILY, 'Oily'),
        (DRY, 'Dry'),
        (DEHYDRATED, 'Dehydrated'),
        (AGING, 'Aging'),
        (TEENAGE, 'Teenage'),
        (BABY, 'Baby'),
        (PROBLEM, 'Problem'),
        (COMBINATION, 'Combination'),
        (FOR_ALL, 'All'),
    )
    skin_type = MultiSelectField(verbose_name='Skin type', choices=SKIN_TYPE, max_length=69)
    FC = 'face'
    EY = 'eyes'
    NK = 'neck'
    BD = 'body'
    HR = 'hair'
    FOR_WHAT = (
        (FC, 'Face'),
        (EY, 'Eyes'),
        (NK, 'Neck'),
        (BD, 'Body'),
        (HR, 'Hair'),
    )
    for_what = MultiSelectField(verbose_name='For what', choices=FOR_WHAT, max_length=24)
    ebay_link = models.CharField(verbose_name='Ebay(link)', max_length=3000)
    blog_link = models.CharField(verbose_name='Blog(link)', max_length=3000)
    youtube_link = models.CharField(verbose_name='Youtube(link)', max_length=3000)

    def __str__(self):
        return f'{self.name} -- {self.brend}'

