# Generated by Django 2.1.8 on 2020-03-26 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Customers', '0007_customerprofile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customerprofile',
            name='email',
            field=models.EmailField(default=1, max_length=100, verbose_name='Email'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='customerprofile',
            name='password',
            field=models.CharField(max_length=20, verbose_name='Password'),
        ),
    ]
