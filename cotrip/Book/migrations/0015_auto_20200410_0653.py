# Generated by Django 2.1.8 on 2020-04-10 06:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0014_auto_20200409_1735'),
    ]

    operations = [
        migrations.AddField(
            model_name='mstbooks',
            name='epub',
            field=models.ImageField(blank=True, null=True, upload_to='epub', verbose_name='Epub'),
        ),
        migrations.AddField(
            model_name='mstbooks',
            name='epub_cover',
            field=models.ImageField(blank=True, null=True, upload_to='epub', verbose_name='Epub Cover'),
        ),
    ]
