from django.db import models
from django.contrib.auth.models import User
from Location.models import CountryMaster, StateMaster, CityMaster
from Configuration.models import CurrencyMaster,BusinessType
from smart_selects.db_fields import ChainedForeignKey
from django.core.validators import RegexValidator
from django.utils.safestring import mark_safe
from mapper.settings import MEDIA_URL


class Company(models.Model):
	auth_user = models.OneToOneField(User, on_delete=models.CASCADE,
            related_name='company_auth_user', null=True,blank=True)
	company_name = models.CharField(max_length=50,verbose_name='Brand Name')
	business_nature = models.ForeignKey(BusinessType,verbose_name='Business Nature',on_delete=models.CASCADE,
							limit_choices_to={
										'active_status': '1'},)
	username = models.CharField(max_length=100, verbose_name='User Name', unique=True)
	password = models.CharField(max_length=20,verbose_name='Password')
	address = models.CharField(max_length=250, verbose_name='Address')
	country = models.ForeignKey(CountryMaster,on_delete=models.CASCADE,related_name='company_country',
							  limit_choices_to={'active_status': '1'},verbose_name='Country')
	state = models.ForeignKey(
		  StateMaster,
		  on_delete=models.CASCADE,
		  related_name='company_state',
		  limit_choices_to={'active_status': '1'},
		  verbose_name='State'
	  )
	city = models.ForeignKey(
		CityMaster,
		on_delete=models.CASCADE,
		related_name='company_city',
		limit_choices_to={'active_status': '1'},
		verbose_name='City',
	  )
	zipcode = models.CharField(max_length=6,verbose_name='PIN Code')
	company_logo = models.ImageField(upload_to='company_logo',
		  null=True, blank=True, verbose_name='Company Logo')
	company_landing_imge = models.ImageField(upload_to='company_banner',
		  null=True, blank=True, verbose_name='Company Banner')
	company_registrationNo = models.CharField(max_length=25,
		  verbose_name='Company Registration No.')
	company_tinnNo = models.CharField(max_length=11, null=True,
		  blank=True, verbose_name='TIN No.')
	company_vatNo = models.CharField(max_length=13, null=True,
		  blank=True, verbose_name='VAT No.')
	company_gstNo = models.CharField(max_length=15, null=True,
		  blank=True, verbose_name='GST No.')
	website = models.URLField(max_length=50, blank=True, null=True,
							verbose_name='Company Website')
	company_contact_no = models.CharField(
		  max_length=15, verbose_name='Contact No.')
	company_email_id = models.EmailField(max_length=50,
		  verbose_name='Contact Email Id')
	support_person = models.CharField(max_length=50,
		  verbose_name='Support Person Name',null=True,blank=True)
	support_person_mobileno = \
	  models.CharField(max_length=15,
					   verbose_name='Support Mobile No.',
					   help_text='Please enter Country /ISD code before mobile number'
					   )
	support_person_email_id = models.EmailField(max_length=255,
		  verbose_name='Support Email ID')
	support_person_landlineno = \
	  models.CharField(max_length=15,
					   verbose_name='Support Landline No.')
	contact_person = models.CharField(max_length=50,
		  verbose_name='Contact Person Name')
	contact_person_mobileno = \
	  models.CharField(max_length=15,
					   verbose_name='Contact Mobile No.',
					   help_text='Please enter Country /ISD code before mobile number'
					   )

	contact_person_email_id = models.EmailField(max_length=255,
		  verbose_name='Contact Other Email ID')
	contact_person_landlineno = \
	  models.CharField(max_length=15,
					   verbose_name='Contact Landline No.')
	owner_name = models.CharField(max_length=50,
								verbose_name='Owner Name')
	owner_email = models.EmailField(max_length=255,
								  verbose_name='Owner Email Id')
	owner_phone = models.CharField(
								 max_length=15,
								 verbose_name='Owner Mobile No.',
								 help_text='Please enter Country /ISD code before mobile number'
								 )
	billing_address = models.CharField(max_length=250,
		  verbose_name='Billing Address', blank=True, null=True)
	is_open = models.BooleanField(default=1, verbose_name='Is Open')
	billing_country = models.ForeignKey(
	  CountryMaster,
	  on_delete=models.CASCADE,
	  related_name='company_billing_country',
	  verbose_name='Billing Country',
	  blank=True,
	  null=True,
	  limit_choices_to={'active_status': '1'},
	  )
	billing_state = models.ForeignKey(
	  StateMaster,
	  on_delete=models.CASCADE,
	  related_name='company_billing_state',
	  verbose_name='Billing State',
	  blank=True,
	  null=True,
	  limit_choices_to={'active_status': '1'},
	  )
	billing_city = models.ForeignKey(
	  CityMaster,
	  on_delete=models.CASCADE,
	  related_name='company_billing_city',
	  verbose_name='Billing City',
	  blank=True,
	  null=True,
	  limit_choices_to={'active_status': '1'},
	  )
	billing_currency = models.ForeignKey(
	  CurrencyMaster,
	  on_delete=models.CASCADE,
	  related_name='company_billing_currency',
	  blank=True,
	  null=True,
	  verbose_name='Billing Currency',
	  limit_choices_to={'active_status': '1'},
	  )
	active_status = models.BooleanField(default=1,verbose_name="Is Active")
	is_sound = models.BooleanField(default=0,verbose_name="Is Sound")
	created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True,verbose_name='Creation Date')
	updated_at = models.DateTimeField(blank=True,null=True,verbose_name='Updation Date')

	class Meta:
		verbose_name = 'Brand'
		verbose_name_plural = 'Brands'

	def __str__(self):
		return self.company_name

	def logo(self):
		if self.company_logo:
			return mark_safe('<img src='+MEDIA_URL+'%s width="50" height="50" />' % (self.company_logo))
			logo.allow_tags = True
		else:
			return 'No Image'
		logo.short_description = 'Company Logo'


	def banner(self):
		if self.company_landing_imge:
			return mark_safe('<img src='+MEDIA_URL+'%s width="50" height="50" />' % (self.company_landing_imge))
			logo.allow_tags = True
		else:
			return 'No Image'
		logo.short_description = 'Company Banner'
