from django.contrib import admin
from Brands.models import Company
from datetime import datetime
from django.contrib.admin import site
from django.forms.utils import ErrorList
from django import forms
from django.contrib.auth.models import User
from Configuration.admin import make_active, make_deactive


def user_create(username, password):
	user_creation = User.objects.create_user(
						username=username,
						password=password,
						is_staff=False,
						is_active=True
						)
	return user_creation

class CompanyAdmin(admin.ModelAdmin):
	exclude = [
			'created_at',
			'updated_at',
			'active_status'
			]
	search_fields = [
		'company_name',
		]
	list_display = [
		  'company_name',
		  'username',
		  'is_open',
		  'address',
		  'country',
		  'state',
		  'city',
		  'logo',
		  'banner',
		  'active_status',
		  'created_at',
		  'updated_at',
			]
	fieldsets = (
	  ('Company Details', {
		  'classes': ('wide', 'extrapretty'),
		  'fields': (
				'company_name',
				'username',
				'password',
				'business_nature',
				'company_logo',
				'company_landing_imge',
				'website'
				)
	  }),
	  ('Address Details', {
		  # 'classes': ('wide',),
		  'fields': (
				'address',
				'country',
				'state',
				'city',
				'zipcode'
				)
	  }),
	  ('Statutory Details', {
		  'fields': (
				'company_registrationNo',
				'company_tinnNo',
				'company_vatNo',
				'company_gstNo'
				)
	  }),
	  ('Contact Details', {
		  'classes': ('wide',),
		  'fields': (
				'company_contact_no',
				'company_email_id',
				'contact_person',
				'contact_person_mobileno',
				'contact_person_email_id',
				'contact_person_landlineno'
				)
	  }),
	  ('Support Details', {
		  'classes': ('wide',),
		  'fields': (
					'support_person',
					'support_person_mobileno',
					'support_person_email_id',
					'support_person_landlineno'
					),
	  }),
	  ('Owner Details', {
		  'classes': ('wide',),
		  'fields': (
					'owner_name',
					'owner_email',
					'owner_phone'
					),
	  }),
	  ('Billing Details', {
		  'classes': ('wide',),
		  'fields': (
				'billing_address',
				'billing_country',
				'billing_state',
				'billing_city',
				'billing_currency'
				),
	  }),

	  
	)
	actions = [make_active, make_deactive]
	list_per_page = 10

	def save_model(self, request, obj, form, change):
		if not change:
			created = user_create(obj.username, obj.password)
			user_id = User.objects.get(id=created.id)
			obj.auth_user = user_id
			obj.save()
		else:
			auth_user = User.objects.filter(id = obj.auth_user_id)
			auth_user.update(username=obj.username)
			for user in auth_user:
				user.set_password(obj.password)
				user.save()
			obj.updated_at = datetime.now()
			obj.save()

	def has_delete_permission(self, request, obj=None):
		return False

	def has_add_permission(self, request, obj=None):
		return True

admin.site.register(Company,CompanyAdmin)

