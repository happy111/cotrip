from django.db import models
from Brands.models import *
from django.core.validators import  MaxValueValidator


class MstAreas(models.Model):
	oversea = models.BooleanField(choices=(
							 ("1", "overseas"),
							 ("0", "domestic"),
							),blank=True,null=True,verbose_name='Oversea')
	area_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='Area Name')
	sort = models.PositiveIntegerField(null=True, blank=True, verbose_name='Sort')
	draft = models.CharField(choices=(
							 ("0", "Unpublished"),
							 ("1", "Editing"),
							 ("2", "Release"),
						),max_length=100,blank=True,null=True,verbose_name='Draft')
	revision = models.PositiveIntegerField(null=True, blank=True, verbose_name='Revision')
	area_code = models.CharField(max_length=150,null=True, blank=True, verbose_name='Area Code')
	status = models.BooleanField(default=0, verbose_name='Is Active')
	created = models.DateTimeField(auto_now_add=True,verbose_name='Creation Date & Time')
	modified = models.DateTimeField(blank=True, null=True,verbose_name='Updation Date & Time')
	deleted = models.DateTimeField(blank=True, null=True,verbose_name='Deleted')


	class Meta:
		verbose_name = 'Master Area'
		verbose_name_plural = ' Master Areas'

	def __str__(self):
		return self.area_name


class MstSeries(models.Model):
	oversea = models.BooleanField(choices=(
							 ("1", "overseas"),
							 ("0", "domestic"),
							),blank=True,null=True,verbose_name='Oversea')			
	series_name = models.CharField(max_length=50, null=True, blank=True, verbose_name='Series Name')
	sort = models.PositiveIntegerField(null=True, blank=True, verbose_name='Sort')
	draft = models.CharField(choices=(
							 ("0", "Unpublished"),
							 ("1", "While editing"),
							 ("2", "Release"),
						),max_length=100,blank=True,null=True,verbose_name='Draft')
	revision = models.PositiveIntegerField(null=True, blank=True, verbose_name='Revision')
	series_code = models.CharField(max_length=150, null=True, blank=True, verbose_name='Series Code')
	status = models.BooleanField(default=0, verbose_name='Is Active')
	created = models.DateTimeField(auto_now_add=True,verbose_name='Creation Date & Time')
	modified = models.DateTimeField(blank=True, null=True,verbose_name='Updation Date & Time')
	deleted = models.DateTimeField(blank=True, null=True,verbose_name='Deleted')



	class Meta:
		verbose_name = 'Master Series'
		verbose_name_plural = ' Master Series'

	def __str__(self):
		return self.series_name

class MstBooks(models.Model):
	isbn_edition = models.CharField(max_length=40,blank=True, null=True,verbose_name="Isbn Edition")
	draft = models.CharField(choices=(
							 ("0", "Unpublished"),
							 ("1", "While editing"),
							 ("2", "Release"),
						),max_length=100,blank=True,null=True,verbose_name='Draft')
	revision = models.PositiveIntegerField(blank=True, null=True,verbose_name="Revision")
	status = models.CharField(max_length=16,blank=True, null=True,verbose_name="Status")
	uuid = models.BigIntegerField(blank=True,null=True,verbose_name="Product Code")
	title = models.CharField(max_length=150,blank=True, null=True,verbose_name="Title")
	issued_date = models.DateField(blank=True, null=True,verbose_name="Issued Date")
	release_date = models.DateField(blank=True, null=True,verbose_name="Release Date")
	oversea = models.BooleanField(choices=(
							 ("1", "overseas"),
							 ("0", "domestic"),
							),blank=True,null=True,verbose_name='Oversea')		
	area_code = models.ForeignKey(MstAreas, related_name='Books_area_code', null=True, blank=True,
										on_delete=models.CASCADE,verbose_name='Area Code',
										limit_choices_to={'status':'1'})

	series_code = models.ForeignKey(MstSeries, related_name='Books_series_code', null=True, blank=True,
												on_delete=models.CASCADE,verbose_name='Series Code',
												limit_choices_to={'status':'1'})

	book_type = models.CharField(
						max_length=100,blank=True,null=True,verbose_name='Draft')

	paper_version = models.CharField(max_length=16, blank=True, null=True)
	item_code_ios = models.CharField(max_length=120, blank=True, null=True)
	item_code_android = models.CharField(max_length=120, blank=True, null=True)
	expiration_start = models.DateField(blank=True, null=True)
	expiration_end = models.DateField(blank=True, null=True,verbose_name='Expiration End')
	expire_days = models.PositiveIntegerField(null=True, blank=True, verbose_name='Expire Days')
	free_url = models.TextField(max_length=200, verbose_name='Free Url',null=True, blank=True)
	browsing_page = models.TextField(max_length=200, verbose_name='Browsing Page',null=True, blank=True)

	explanation = models.TextField(max_length=4000, verbose_name='Explanation',null=True, blank=True)
	map_credit = models.TextField(max_length=4000, verbose_name='Map Credit',null=True, blank=True)
	page_direction = models.CharField(max_length=150, blank=True, null=True,verbose_name='Page Direction')
	data_path = models.CharField(max_length=240, blank=True, null=True,verbose_name='Data Path')
	status = models.BooleanField(default=0, verbose_name='Is Active')
	created = models.DateTimeField(auto_now_add=True,verbose_name='Creation Date & Time')
	modified = models.DateTimeField(blank=True, null=True,verbose_name='Updation Date & Time')
	deleted = models.DateTimeField(blank=True, null=True,verbose_name='Deleted')
	epub = models.FileField(upload_to='epub',
								null=True, blank=True, verbose_name='Epub')
	epub_cover = models.FileField(upload_to='epubcover',
								null=True, blank=True, verbose_name='Epub Cover')



	class Meta:
		verbose_name = 'Master Books'
		verbose_name_plural = ' Master Books'

	def __str__(self):
		return str(self.title)






class OnetimeLinks(models.Model):
    created = models.DateTimeField(auto_now_add=True,verbose_name='Creation Date & Time')
    modified = models.DateTimeField(blank=True, null=True,verbose_name='Updation Date & Time')
    deleted = models.DateTimeField(blank=True, null=True,verbose_name='Deleted')
    isbn_edition = models.CharField(max_length=40,blank=True, null=True,verbose_name="Isbn Edition")
    onetime_key = models.CharField(max_length=80,blank=True , null =True , verbose_name="One Time key")
    expire_date = models.DateField(null=True, blank=True, verbose_name='Expire Date')
    limited_count = models.IntegerField()
    used = models.IntegerField()
    administrator = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'onetime_links'