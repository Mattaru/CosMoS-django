# Generated by Django 3.1.7 on 2021-06-21 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='country',
            name='flag_img_name',
            field=models.CharField(blank=True, max_length=125, null=True, verbose_name='flag image name'),
        ),
    ]
