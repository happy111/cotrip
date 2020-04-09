# Generated by Django 2.1.8 on 2020-04-06 10:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0012_auto_20200406_0240'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='mstbooktourareas',
            name='isbn_edition',
        ),
        migrations.RenameField(
            model_name='mstbooks',
            old_name='product_code',
            new_name='uuid',
        ),
        migrations.RemoveField(
            model_name='mstbooks',
            name='contents_version',
        ),
        migrations.RemoveField(
            model_name='mstbooks',
            name='dl_map_enabled',
        ),
        migrations.RemoveField(
            model_name='mstbooks',
            name='location',
        ),
        migrations.RemoveField(
            model_name='mstbooks',
            name='map_enabled',
        ),
        migrations.RemoveField(
            model_name='mstbooks',
            name='paper_enabled',
        ),
        migrations.RemoveField(
            model_name='mstbooks',
            name='station_enabled',
        ),
        migrations.DeleteModel(
            name='MstBookTourareas',
        ),
    ]