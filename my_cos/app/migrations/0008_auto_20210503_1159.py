# Generated by Django 3.1.7 on 2021-05-03 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0007_auto_20210503_1124'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.ImageField(default='unknown.png', upload_to='product_img/%name', verbose_name='image'),
        ),
    ]
