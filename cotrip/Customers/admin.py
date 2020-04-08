from django.contrib import admin
from django.db.models import Q
from Customers.models import CustomerProfile, customer_otp
import datetime
from django.contrib.auth.models import User
# Register your models here.

def make_active(modeladmin, request, queryset):
	queryset.update(active_status='1',updated_at=datetime.datetime.now())
make_active.short_description = "Move Items to Active"

def make_deactive(modeladmin, request, queryset):
	queryset.update(active_status='0',updated_at=datetime.datetime.now())
make_deactive.short_description = "Move Items to Deactive"


def user_create(username, password):
	user_creation = User.objects.create_user(
						username=username,
						password=password,
						is_staff=False,
						is_active=True
						)
	return user_creation



class CustomerAdmin(admin.ModelAdmin):

	exclude = [
		'authuser',
		'active_status',
		'created_at',
		'updated_at', 
		'age',
		'user_type',
		'auth_user',
		'username',
		'mobile',
		'last_logined',
		'deleted'


	]
	list_filter = ['active_status']
	search_fields = ['nickname', 'email']
	list_display = [
		'nickname',
		'email',
		"typesuser",
		'active_status',
		'created_at',
		'updated_at'
	]
	readonly_fields = [

	]

	actions = [make_active,make_deactive]
	list_per_page = 10

	def has_delete_permission(self, request, obj=None):
		return False

	def has_add_permission(self, request, obj=None):
		return True

	def save_model(self, request, obj, form, change):
		if not change:
			company = str(1)
			username = company +'M'+str(obj.email)
			print("sssssssssssss",username)
			created = user_create(username, obj.password)
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


class CustomerOTPAdmin(admin.ModelAdmin):
	list_filter = ['is_mobile_verified', 'is_email_verfied']
	# search_fields = ['username', 'email', 'mobile']
	list_display = [
		'customer', 
		'mobile_OTP',
		'email_OTP',
		'is_mobile_verified',
		'is_email_verfied',
		'is_email_otp_used',
		'is_mob_otp_used',
		'created_at',
		# 'updated_at'
	]
	readonly_fields = [
		'customer', 
		'mobile_OTP',
		'email_OTP',
		'is_mobile_verified',
		'is_email_verfied',	
	]


	def has_delete_permission(self, request, obj=None):
		return False

	def has_add_permission(self, request, obj=None):
		return False

	def save_model(self, request, obj, form, change):
		obj.save()

admin.site.register(CustomerProfile,CustomerAdmin)
# admin.site.register(customer_otp,CustomerOTPAdmin)