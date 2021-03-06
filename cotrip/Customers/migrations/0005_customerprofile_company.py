# Generated by Django 2.1.8 on 2020-03-24 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Brands', '0001_initial'),
        ('Customers', '0004_customerprofile_gender'),
    ]

    operations = [
        migrations.AddField(
            model_name='customerprofile',
            name='company',
            field=models.ForeignKey(default=1, limit_choices_to={'active_status': '1'}, on_delete=django.db.models.deletion.CASCADE, related_name='CustomerProfile_Company', to='Brands.Company', verbose_name='Company'),
            preserve_default=False,
        ),
    ]
