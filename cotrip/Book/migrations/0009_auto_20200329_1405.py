# Generated by Django 2.1.8 on 2020-03-29 14:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0008_auto_20200329_1350'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mstareas',
            name='oversea',
            field=models.CharField(blank=True, choices=[('0', 'overseas'), ('1', 'domestic')], max_length=100, null=True, verbose_name='Oversea'),
        ),
        migrations.AlterField(
            model_name='mstbooks',
            name='oversea',
            field=models.CharField(blank=True, choices=[('0', 'overseas'), ('1', 'domestic')], max_length=100, null=True, verbose_name='Oversea'),
        ),
        migrations.AlterField(
            model_name='mstseries',
            name='oversea',
            field=models.CharField(blank=True, choices=[('0', 'overseas'), ('1', 'domestic')], max_length=100, null=True, verbose_name='Oversea'),
        ),
    ]
