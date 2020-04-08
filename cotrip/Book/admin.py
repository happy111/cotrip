from django.contrib import admin
from Book.models import *



def make_active(modeladmin, request, queryset):
	queryset.update(status='1',modified=datetime.now())
make_active.short_description = "Move Items to Active"

def make_deactive(modeladmin, request, queryset):
	queryset.update(status='0',modified=datetime.now())
make_deactive.short_description = "Move Items to Deactive"


class MstAreasAdmin(admin.ModelAdmin):
	exclude = [
	
			]
	search_fields = [
					'area_name',
					'area_code'
				]
	list_display = [
					'area_name',
					'area_code'
				]

	actions = [make_active, make_deactive]
	list_per_page = 10

	def save_model(self, request, obj, form, change):
		if not change:
			obj.created = datetime.now()
		else:
			obj.modified = datetime.now()
		obj.save()
	def has_delete_permission(self, request, obj=None):
		return False
	def has_add_permission(self, request, obj=None):
		return False


class MstSeriesAdmin(admin.ModelAdmin):
	exclude = [
	
			]
	search_fields = [
					'series_name',
					'series_code'
				]
	list_display = [
					'series_name',
					'series_code'
				]

	actions = [make_active, make_deactive]
	list_per_page = 10

	def save_model(self, request, obj, form, change):
		if not change:
			obj.created = datetime.now()
		else:
			obj.modified = datetime.now()
		obj.save()
	def has_delete_permission(self, request, obj=None):
		return False
	def has_add_permission(self, request, obj=None):
		return False


class MstBooksAdmin(admin.ModelAdmin):
	exclude = [
	
			]
	search_fields = [
					'book_type',
					'uuid'
				]
	list_display = [
					'title',
					'book_type',
					'uuid'
				]

	actions = [make_active, make_deactive]
	list_per_page = 10

	def save_model(self, request, obj, form, change):
		if not change:
			obj.created = datetime.now()
		else:
			obj.modified = datetime.now()
		obj.save()
	def has_delete_permission(self, request, obj=None):
		return False
	def has_add_permission(self, request, obj=None):
		return False

admin.site.register(MstAreas,MstAreasAdmin)
admin.site.register(MstSeries,MstSeriesAdmin)
admin.site.register(MstBooks,MstBooksAdmin)