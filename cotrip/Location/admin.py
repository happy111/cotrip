from django.contrib import admin
from Location.models import CountryMaster, StateMaster, CityMaster, AreaMaster
from django import forms
from datetime import datetime
from Configuration.admin import make_active, make_deactive
from django.forms.utils import ErrorList
from rangefilter.filter import DateRangeFilter, DateTimeRangeFilter


class CountryMasterAdmin(admin.ModelAdmin):
	exclude = [
		'active_status',
		'created_at',
		'updated_at',
	  ]

	list_filter = [
			'active_status',
		('created_at', DateRangeFilter),
		('updated_at', DateRangeFilter),'currency__currency'
		]

	search_fields = [
	  'country',
	  'currency__currency'
	  ]

	list_display = [
	  'country',
	  'currency',
	  'mobile_no_digits',
	  'active_status',
	  'created_at', 
	  'updated_at',
	  ]

	actions = [make_active, make_deactive]

	list_per_page = 10

	def has_delete_permission(self, request, obj=None):
		return False

	def save_model(self, request, obj, form, change):
		if not change:
			obj.created_at = datetime.now()
		else:
			obj.updated_at = datetime.now()
		obj.save()


class StateMasterAdmin(admin.ModelAdmin):
	# form = StateMasterForm
	list_filter = [
		'active_status',
		'country__country', 
	   ('created_at', DateRangeFilter), 
	   ('updated_at', DateRangeFilter),]
	search_fields = ['state',]
	exclude = [
		  'active_status',
		  'created_at',
		  'updated_at',
		  ]
	list_display = [
			'state',
			'country',
			'active_status',
			'created_at', 
			'updated_at',
			]

	actions = [make_active, make_deactive]

	list_per_page = 10

	def has_delete_permission(self, request, obj=None):
		return False

	def save_model(self, request, obj, form, change):
		if not change:
			obj.created_at = datetime.now()
		else:
			obj.updated_at = datetime.now()
		obj.save()


class CityMasterAdmin(admin.ModelAdmin):
	list_filter = [
	  'active_status',
	  'state',
	  ('created_at', DateRangeFilter), 
	  ('updated_at', DateRangeFilter),
	  ]
	search_fields = ['city',]
	exclude = [
	  'active_status',
	  'created_at',
	  'updated_at',
	  ]
	list_display = [
	  'city', 
	  'state',
	  'active_status',
	  'created_at', 
	  'updated_at',
	  ]

	actions = [make_active, make_deactive]

	list_per_page = 10

	def has_delete_permission(self, request, obj=None):
		return False

	def save_model(self, request, obj, form, change):
		if not change:
			obj.created_at = datetime.now()
		else:
			obj.updated_at = datetime.now()
		obj.save()

class AreaMasterAdmin(admin.ModelAdmin):
	list_filter = [
	  'active_status',
	  ('created_at', DateRangeFilter), 
	  ('updated_at', DateRangeFilter),
	  ]
	search_fields = ['area',]
	exclude = [
	  'active_status',
	  'created_at',
	  'updated_at',
	  ]
	list_display = [
	  'area',
	  'city', 
	  'active_status',
	  'created_at', 
	  'updated_at',
	  ]

	actions = [make_active, make_deactive]

	list_per_page = 10

	def has_delete_permission(self, request, obj=None):
		return False

	def save_model(self, request, obj, form, change):
		if not change:
			obj.created_at = datetime.now()
		else:
			obj.updated_at = datetime.now()
		obj.save()

admin.site.register(CountryMaster,CountryMasterAdmin)
admin.site.register(StateMaster,StateMasterAdmin)
admin.site.register(CityMaster,CityMasterAdmin)
admin.site.register(AreaMaster,AreaMasterAdmin)

