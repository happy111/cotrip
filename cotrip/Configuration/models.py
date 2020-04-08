from django.db import models
from django.core.validators import RegexValidator
from django.contrib.auth.models import User


class BusinessType(models.Model):
	business_type = models.CharField(max_length=50, verbose_name='Business Type',
	                                           unique=True)
	description = models.CharField(max_length=200, null=True, blank=True, verbose_name=
		                                                        'Description')
	active_status = models.BooleanField(default=1, verbose_name='Is Active')
	created_at = models.DateTimeField(auto_now_add=True,verbose_name='Creation Date & Time')
	updated_at = models.DateTimeField(null=True, blank=True, verbose_name=
																			'Updation Date & Time')

	class Meta:
		verbose_name = '    Brand Type'
		verbose_name_plural = '    Brand Types'
		ordering = ['business_type']


	def __str__(self):
		return self.business_type


class CurrencyMaster(models.Model):
	currency = models.CharField(max_length=30, unique=True,
	    error_messages={'unique':"Currency already exists with the given name."}, 
	                      verbose_name="Currency")
	symbol = models.CharField(max_length=20, verbose_name="Symbol")
	hexsymbol = models.CharField(max_length=7, verbose_name='Hex Symbol',
		                                                   blank=True, null=True)
	active_status = models.BooleanField(default=1, verbose_name='Is Active')
	created_at = models.DateTimeField(auto_now_add=True,verbose_name='Creation Date & Time')
	updated_at = models.DateTimeField(null=True, blank=True, verbose_name=
																			'Updation Date & Time')

	class Meta:
		verbose_name = "   Currency"
		verbose_name_plural = "   Currencies"

	def __str__(self):
		return self.currency




class Excelimport(models.Model):
	title = models.CharField(max_length=255,null=True, blank=True, verbose_name="Title")
	image = models.ImageField(upload_to='import',null=True, blank=True, verbose_name='image')
	active_status = models.BooleanField(default=1, verbose_name='Is Active')
	created_at = models.DateTimeField(auto_now_add=True,verbose_name='Creation Date & Time')
	updated_at = models.DateTimeField(null=True, blank=True, verbose_name=
																			'Updation Date & Time')

	class Meta:
		verbose_name = "   Excel Import"
		verbose_name_plural = "   Excel Import"

	def __str__(self):
		return str(self.title)








