# Generated by Django 3.1.7 on 2021-03-30 08:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_auto_20210330_1109'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='consistency',
            new_name='ingredients',
        ),
        migrations.RenameField(
            model_name='product',
            old_name='consistency_img',
            new_name='ingredients_img',
        ),
    ]
