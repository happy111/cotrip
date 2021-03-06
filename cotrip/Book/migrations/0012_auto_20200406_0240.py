# Generated by Django 2.1.8 on 2020-04-06 02:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0011_auto_20200331_0958'),
    ]

    operations = [
        migrations.CreateModel(
            name='OnetimeLinks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date & Time')),
                ('modified', models.DateTimeField(blank=True, null=True, verbose_name='Updation Date & Time')),
                ('deleted', models.DateTimeField(blank=True, null=True, verbose_name='Deleted')),
                ('isbn_edition', models.CharField(blank=True, max_length=40, null=True, verbose_name='Isbn Edition')),
                ('onetime_key', models.CharField(blank=True, max_length=80, null=True, verbose_name='One Time key')),
                ('expire_date', models.DateField(blank=True, null=True, verbose_name='Expire Date')),
                ('limited_count', models.IntegerField()),
                ('used', models.IntegerField()),
                ('administrator', models.TextField(blank=True, null=True)),
            ],
            options={
                'db_table': 'onetime_links',
                'managed': False,
            },
        ),
        migrations.AlterField(
            model_name='mstbooks',
            name='book_type',
            field=models.CharField(blank=True, max_length=100, null=True, verbose_name='Draft'),
        ),
        migrations.AlterField(
            model_name='mstbooks',
            name='expiration_end',
            field=models.DateField(blank=True, null=True, verbose_name='Expiration End'),
        ),
        migrations.AlterField(
            model_name='mstbooks',
            name='explanation',
            field=models.TextField(blank=True, max_length=4000, null=True, verbose_name='Explanation'),
        ),
        migrations.AlterField(
            model_name='mstbooks',
            name='map_credit',
            field=models.TextField(blank=True, max_length=4000, null=True, verbose_name='Map Credit'),
        ),
        migrations.AlterField(
            model_name='mstbooks',
            name='product_code',
            field=models.BigIntegerField(blank=True, null=True, verbose_name='Product Code'),
        ),
    ]
