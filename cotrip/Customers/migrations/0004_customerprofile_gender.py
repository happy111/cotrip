# Generated by Django 2.1.8 on 2020-03-24 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customers', '0003_auto_20200324_1058'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerprofile',
            name='gender',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Gender'),
        ),
    ]
