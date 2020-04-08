# Generated by Django 2.1.8 on 2020-03-28 07:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Book', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='MstBooks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('isbn_edition', models.CharField(blank=True, max_length=40, null=True, verbose_name='Isbn Edition')),
                ('draft', models.PositiveIntegerField(blank=True, null=True, verbose_name='Draft')),
                ('revision', models.PositiveIntegerField(blank=True, null=True, verbose_name='Revision')),
                ('product_code', models.PositiveIntegerField(blank=True, null=True, verbose_name='Product Code')),
                ('title', models.CharField(blank=True, max_length=150, null=True, verbose_name='Title')),
                ('issued_date', models.DateField(blank=True, null=True, verbose_name='Issued Date')),
                ('release_date', models.DateField(blank=True, null=True, verbose_name='Release Date')),
                ('oversea', models.PositiveIntegerField(blank=True, null=True, verbose_name='Oversea')),
                ('book_type', models.CharField(blank=True, max_length=200, null=True, verbose_name='Book Type')),
                ('paper_version', models.CharField(blank=True, max_length=16, null=True)),
                ('contents_version', models.CharField(blank=True, max_length=16, null=True)),
                ('location', models.TextField(blank=True, null=True, verbose_name='Location')),
                ('item_code_ios', models.CharField(blank=True, max_length=120, null=True)),
                ('item_code_android', models.CharField(blank=True, max_length=120, null=True)),
                ('expiration_start', models.DateField(blank=True, null=True)),
                ('expiration_end', models.DateTimeField(blank=True, null=True, verbose_name='Expiration End')),
                ('expire_days', models.PositiveIntegerField(blank=True, null=True, verbose_name='Expire Days')),
                ('free_url', models.TextField(blank=True, max_length=200, null=True, verbose_name='Free Url')),
                ('browsing_page', models.TextField(blank=True, max_length=200, null=True, verbose_name='Browsing Page')),
                ('paper_enabled', models.PositiveIntegerField(blank=True, null=True, verbose_name='Paper Enabled')),
                ('map_enabled', models.PositiveIntegerField(blank=True, null=True, verbose_name='Map Enabled')),
                ('dl_map_enabled', models.PositiveIntegerField(blank=True, null=True, verbose_name='DL Map Enabled')),
                ('station_enabled', models.PositiveIntegerField(blank=True, null=True, verbose_name='Station Enabled')),
                ('explanation', models.TextField(blank=True, max_length=200, null=True, verbose_name='Explanation')),
                ('map_credit', models.TextField(blank=True, max_length=200, null=True, verbose_name='Map Credit')),
                ('page_direction', models.CharField(blank=True, max_length=150, null=True, verbose_name='Page Direction')),
                ('data_path', models.CharField(blank=True, max_length=240, null=True, verbose_name='Data Path')),
                ('status', models.BooleanField(default=0, verbose_name='Is Active')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='Creation Date & Time')),
                ('modified', models.DateTimeField(blank=True, null=True, verbose_name='Updation Date & Time')),
                ('deleted', models.DateTimeField(blank=True, null=True, verbose_name='Deleted')),
                ('area_code', models.ForeignKey(blank=True, limit_choices_to={'status': '1'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Books_area_code', to='Book.MstAreas', verbose_name='Area Code')),
                ('series_code', models.ForeignKey(blank=True, limit_choices_to={'status': '1'}, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='Books_series_code', to='Book.MstSeries', verbose_name='Series Code')),
            ],
            options={
                'verbose_name': 'Master Books',
                'verbose_name_plural': ' Master Books',
            },
        ),
    ]
