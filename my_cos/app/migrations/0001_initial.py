# Generated by Django 3.1.7 on 2021-05-08 12:45

import app.models
from django.db import migrations, models
import django.db.models.deletion
import multiselectfield.db.fields
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Country',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=100, unique=True, verbose_name='country name')),
                ('slug', models.SlugField(max_length=100, null=True, unique=True)),
                ('flag_img_name', models.CharField(blank=True, max_length=50, null=True, verbose_name='flag image name')),
            ],
            options={
                'verbose_name': 'Country',
                'verbose_name_plural': 'Countries',
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='ingredient name')),
                ('slug', models.SlugField(max_length=200, null=True, unique=True)),
                ('description', models.TextField()),
                ('safety_classification', models.CharField(blank=True, choices=[(None, 'Absent'), ('safe', 'Safe'), ('neutral', 'Neutral'), ('harmful', 'Harmful')], max_length=7, null=True, verbose_name='safety classification')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='date')),
                ('approved', models.BooleanField(default=False, verbose_name='approved')),
            ],
            options={
                'verbose_name': 'Ingredient',
                'verbose_name_plural': 'Ingredients',
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('brand', models.CharField(blank=True, max_length=100, null=True, verbose_name='brand')),
                ('line', models.CharField(blank=True, max_length=100, null=True, verbose_name='line')),
                ('name', models.CharField(max_length=200, unique=True, verbose_name='product name')),
                ('slug', models.SlugField(max_length=200, null=True, unique=True)),
                ('img', models.ImageField(default='unknown.png', upload_to=app.models.get_img_upload_path, verbose_name='image')),
                ('ingredients', models.TextField(verbose_name='ingredients')),
                ('ph', models.CharField(blank=True, choices=[(None, 'Absent'), ('4', '4'), ('4.5', '4.5'), ('5', '5'), ('5.5', '5.5'), ('6', '6'), ('6.5', '6.5'), ('7', '7'), ('7.5', '7.5'), ('8', '8'), ('8.5', '8.5'), ('9', '9')], max_length=3, null=True, verbose_name='ph')),
                ('effect_type', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('calming', 'Calming'), ('anti wrinkle', 'Anti wrinkle'), ('skin elasticity', 'Skin elasticity'), ('moisturizing', 'Moisturizing'), ('skin microbiome', 'Skin microbiome'), ('sun protection', 'Sun protection'), ('lifting', 'Lifting'), ('healing', 'Healing'), ('antipigmentation', 'Antipigmentation')], max_length=113, null=True, verbose_name='effect type')),
                ('skin_type', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('normal', 'Normal'), ('oily', 'Oily'), ('dry', 'Dry'), ('dehydrated', 'Dehydrated'), ('aging', 'Aging'), ('teenage', 'Teenage'), ('baby', 'Baby'), ('problem', 'Problem'), ('combination', 'Combination'), ('all', 'All')], max_length=69, null=True, verbose_name='skin type')),
                ('for_what', multiselectfield.db.fields.MultiSelectField(blank=True, choices=[('face', 'Face'), ('eyes', 'Eyes'), ('neck', 'Neck'), ('body', 'Body'), ('hair', 'Hair')], max_length=24, null=True, verbose_name='for what')),
                ('ebay_link', models.CharField(blank=True, max_length=3000, null=True, verbose_name='ebay(link)')),
                ('amazon_link', models.CharField(blank=True, max_length=3000, null=True, verbose_name='amazon(link)')),
                ('blog_link', models.CharField(blank=True, default='https://beauty-granny.com', max_length=3000, verbose_name='blog(link)')),
                ('youtube_link', models.CharField(blank=True, max_length=3000, null=True, verbose_name='youtube(link)')),
                ('facebook_link', models.CharField(blank=True, max_length=3000, null=True, verbose_name='facebook(link)')),
                ('telegram_link', models.CharField(blank=True, max_length=3000, null=True, verbose_name='telegram(link)')),
                ('instagram_link', models.CharField(blank=True, max_length=3000, null=True, verbose_name='instagram(link)')),
                ('creation_date', models.DateTimeField(auto_now_add=True, verbose_name='date')),
                ('approved', models.BooleanField(default=False, verbose_name='approved')),
                ('country', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='Product_country', to='app.country', verbose_name='country')),
                ('ingredients_list', models.ManyToManyField(blank=True, to='app.Ingredient')),
            ],
            options={
                'verbose_name': 'Product',
                'verbose_name_plural': 'Products',
                'ordering': ['name', '-creation_date'],
            },
        ),
    ]
