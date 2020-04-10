from django.db import models
from django.contrib.auth.models import User
from Location.models import CountryMaster, StateMaster,CityMaster,AreaMaster
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.safestring import mark_safe
from mapper.settings import MEDIA_URL
from smart_selects.db_fields import ChainedForeignKey
from django.contrib.auth.models import AbstractBaseUser
from Brands.models import Company
from django.contrib.postgres.fields import JSONField


class CustomerProfile(models.Model):
	auth_user = models.OneToOneField(User, on_delete=models.CASCADE,
			related_name='CustomerProfile_auth_user',null=True,blank=True)
	company = models.ForeignKey(Company, related_name='CustomerProfile_Company', null=True, blank=True,
												on_delete=models.CASCADE,verbose_name='Company',
												limit_choices_to={'active_status':'1'})
	nickname = models.CharField(max_length=100,null=True,blank=True, verbose_name='Nick Name')
	prefecture = models.CharField(max_length=100, verbose_name='Prefecture',null=True,blank=True)

	username = models.CharField(max_length=100, verbose_name='User Name',null=True,blank=True)
	password = models.CharField(max_length=100, verbose_name='Password',null=True,blank=True)

	mobile = models.CharField(max_length=20,
			verbose_name='Mobile No',null=True,blank=True)


	user_type = models.BooleanField(default=1, verbose_name='User Type')


	email = models.EmailField(max_length=100,null=True,blank=True, verbose_name='Email')
	gender = models.CharField(max_length=100,verbose_name='Gender', null=True, blank=True)
	birth_year = models.DateTimeField(verbose_name='Birth Year', null=True,blank=True)
	age = models.PositiveIntegerField(validators=[MinValueValidator(18),MaxValueValidator(100),], 
						verbose_name='Age', null=True, blank=True)
	twitter_id = models.CharField(max_length=50, null=True, blank=True, verbose_name='twitter_id')
	facebook_id = models.CharField(max_length=50, null=True, blank=True, verbose_name='facebook_id')
	married = models.BooleanField(default=0, verbose_name='married')

	job = models.CharField(max_length=100, verbose_name='Job',null=True,blank=True)

	allow_mail = models.BooleanField(default=0, verbose_name='Allow Mail')
	active_status = models.BooleanField(default=0, verbose_name='Is Active')
	created_at = models.DateTimeField(auto_now_add=True,verbose_name='Creation Date & Time')
	updated_at = models.DateTimeField(blank=True, null=True,verbose_name='Updation Date & Time')
	last_logined = models.DateTimeField(blank=True, null=True,verbose_name='Last Logind')
	deleted = models.DateTimeField(blank=True, null=True,verbose_name='Deleted')



	class Meta:
		verbose_name = 'Customer'
		verbose_name_plural = ' Customer Profiles'

	def __str__(self):
		return self.email

	def typesuser(self):
		if self.user_type == 1:
			a = "Admin"
		else:
			a = "Normal User"
		return a
		
	typesuser.short_description = 'User Type'




class customer_otp(models.Model):
	customer = models.ForeignKey(CustomerProfile,on_delete=models.CASCADE,
		related_name='customer_customer',verbose_name='Customer', null=True, blank=True)
	mobile_OTP = \
	models.CharField(max_length=10, verbose_name = 'Mobile OTP', null=True, blank=True,)
	email_OTP = \
	models.CharField(max_length=10, verbose_name = 'Email OTP', null=True, blank=True,)
	is_mobile_verified = models.BooleanField(default=False,verbose_name='Is Mobile Number Verified')
	is_email_verfied = models.BooleanField(default=False,verbose_name='Is Email Verified')
	is_email_otp_used = models.BooleanField(default=False,verbose_name='Is Email OTP Used')
	is_mob_otp_used = models.BooleanField(default=False,verbose_name='Is Mobile OTP Used')
	created_at = models.DateTimeField(auto_now_add=True,verbose_name='Creation Date')

	class Meta:
		verbose_name = ' Customer OTP'
		verbose_name_plural = 'Customer OTP'

	def __int__(self):
		return self.customer
