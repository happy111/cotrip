# Generated by Django 2.1.8 on 2020-03-29 13:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0007_auto_20200329_0538'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mstareas',
            name='area_code',
            field=models.CharField(blank=True, max_length=150, null=True, verbose_name='Area Code'),
        ),
    ]
