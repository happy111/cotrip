# Generated by Django 2.1.8 on 2020-03-26 11:17

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customers', '0012_auto_20200326_1116'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerprofile',
            name='age',
            field=models.PositiveIntegerField(blank=True, null=True, validators=[django.core.validators.MinValueValidator(18), django.core.validators.MaxValueValidator(100)], verbose_name='Age'),
        ),
    ]
