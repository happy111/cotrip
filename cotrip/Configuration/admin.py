from django.contrib import admin
from Configuration.models import *
from datetime import datetime
from django.contrib.admin import site


def make_active(modeladmin, request, queryset):
	queryset.update(active_status='1',updated_at=datetime.now())
make_active.short_description = "Move Items to Active"

def make_deactive(modeladmin, request, queryset):
	queryset.update(active_status='0',updated_at=datetime.now())
make_deactive.short_description = "Move Items to Deactive"



class BusinessTypeAdmin(admin.ModelAdmin):
	exclude = [
			'active_status',
			'created_at',
			'updated_at',
			]
	search_fields = ['business_type']
	list_filter = [
				'active_status',
				'created_at', 
				'updated_at'
				]
	list_display=[
				'business_type',
				'description',
				'active_status',
				'created_at', 
				'updated_at',
				]
	actions = [
			make_active,
			make_deactive,
			]
	list_per_page = 10

	def has_delete_permission(self, request, obj=None):
		return False

	def save_model(self, request, obj, form, change):
		if not change:
			obj.created_by = request.user
		else:
			obj.updated_by = request.user
			obj.updated_at = datetime.now()
		obj.save()



class CurrencyMasterAdmin(admin.ModelAdmin):
	exclude = [
			'active_status',
			'created_at',
			'updated_at',
			]
	search_fields = ['currency']
	list_filter = [
				'active_status',
				'created_at', 
				'updated_at'
				]
	list_display=[
				'currency',
				'symbol',
				'hexsymbol', 
				'active_status',
				'created_at'
				]
	actions = [
			make_active,
			make_deactive,
			]
	list_per_page = 10

	def has_delete_permission(self, request, obj=None):
		return False

	def save_model(self, request, obj, form, change):
		if not change:
			obj.created_at = datetime.now()
		else:
			obj.updated_at = datetime.now()
		obj.save()








admin.site.register(BusinessType, BusinessTypeAdmin)
admin.site.register(CurrencyMaster, CurrencyMasterAdmin)
