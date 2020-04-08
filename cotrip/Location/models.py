from django.db import models
from django.contrib.auth.models import User
from Configuration.models import CurrencyMaster
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils.safestring import mark_safe
from mapper.settings import MEDIA_URL


class CountryMaster(models.Model):
    country = models.CharField(max_length=35,unique=True,verbose_name='Country')
    iso = models.CharField(max_length=4,verbose_name='ISO')
    isd = models.PositiveIntegerField(validators=[MaxValueValidator(999999),MinValueValidator(1)],
    									verbose_name='ISD/Country Code')
    currency = models.ForeignKey(CurrencyMaster,on_delete=models.CASCADE,related_name='country_master_currency',
    								verbose_name='Currency',limit_choices_to={'active_status': '1'})
    mobile_no_digits = models.PositiveIntegerField(validators=[MaxValueValidator(15),MinValueValidator(5)],
    												verbose_name='Countries Mobile Number digit')
    country_flag = models.ImageField(upload_to='countryflag/',verbose_name='Country Flag',null=True,blank=True)
    active_status = models.BooleanField(default=1,verbose_name="Is Active")
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True,verbose_name='Creation Date')
    updated_at = models.DateTimeField(blank=True,null=True,verbose_name='Updation Date')

    def flag_image(self):
        if self.country_flag:
            return mark_safe('<img src='+MEDIA_URL+'%s width="50" height="50" />' % (self.country_flag))
        return 'No Image'
    flag_image.short_description = 'Country Flag'

    class Meta:
        verbose_name = '   Country'
        verbose_name_plural = '   Countries'
        ordering = ['country']

    def isd_country_code(self):
        if self.isd:
            return "+"+str(self.isd)
        return "-"
    isd_country_code.short_description = 'ISD/Country Code'

    def __str__(self):
        return self.country


class StateMaster(models.Model):
    state = models.CharField(max_length=35,verbose_name='State')
    country = models.ForeignKey(CountryMaster,related_name='state_master_state',on_delete=models.CASCADE,
    				null=True,verbose_name='Country',limit_choices_to={'active_status': '1'})
    short_name = models.CharField(max_length=35, verbose_name='Short Name')
    active_status = models.BooleanField(default=1,verbose_name="Is Active")
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True,verbose_name='Creation Date')
    updated_at = models.DateTimeField(blank=True,null=True,verbose_name='Updation Date')

    class Meta:
        unique_together = ('country', 'state')
        verbose_name = '  State'
        verbose_name_plural = '  States'
        ordering = ['state']

    def __str__(self):
        return self.state


class CityMaster(models.Model):
    city = models.CharField(max_length=35, verbose_name='City')
    state = models.ForeignKey(StateMaster,related_name='city_master_city',on_delete=models.CASCADE,
    								verbose_name='State',limit_choices_to={'active_status': '1'})
    active_status = models.BooleanField(default=1,verbose_name="Is Active")
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True,verbose_name='Creation Date')
    updated_at = models.DateTimeField(blank=True,null=True,verbose_name='Updation Date')

    class Meta:
        unique_together = ('state', 'city')
        verbose_name = ' City'
        verbose_name_plural = ' Cities'
        ordering = ['city']

    def __str__(self):
        return self.city



class AreaMaster(models.Model):
    area = models.CharField(max_length=100, verbose_name='City Area')
    city = models.ForeignKey(CityMaster,related_name='city_area_city',on_delete=models.CASCADE,
        					verbose_name='City',limit_choices_to={'active_status': '1'})
    active_status = models.BooleanField(default=1,verbose_name="Is Active")
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True,verbose_name='Creation Date')
    updated_at = models.DateTimeField(blank=True,null=True,verbose_name='Updation Date')

    class Meta:
        verbose_name = 'Locality'
        verbose_name_plural = 'Localities'
        ordering = ['area']

    def __str__(self):
        return self.area
