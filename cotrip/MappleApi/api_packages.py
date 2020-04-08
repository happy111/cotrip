from datetime import datetime
import re
from django.db.models import Sum
import string

zero__re = r'[0]*$'
alpha_re = r"[a-zA-Z' ]*$"
alpha_nu_re = r"[a-zA-Z' ]{1,}[0-9,- ]{0,}[a-zA-Z']{1,}*$"
vat_re = r'[a-zA-Z.0-9 ]*$'
contact_re = r'[0-9]*$'
res_limit_re = r'[0-9]{1,5}$'
address_re = r'[a-zA-z0-9]{1,250}[.&,()/\ -]{0,}[a-zA-z.0-9&,()/\ -]{1,250}$'
lat_long_re = r'[0-9-]{1,}[.]{0,}[0-9-.]{0,15}$'
description_re = r"[a-zA-z0-9 ]{1,}[@%&$.,/\()!|'#* -]{0,}[a-zA-z.,#@%&$/\()|!'0-9 -;]{0,}$"
cu_service_re = r"[a-zA-z0-9;]{1,200}[@%&$.,/\()' -]{0,}[a-zA-z.,@%&$/\()'0-9 -;]{0,200}$"
email_re = r'[a-zA-Z0-9]{1,}[._]{0,}[a-zA-Z0-9]{1,}[@]{1,1}[a-zA-Z0-9]{1,}[.]{1,1}[a-zA-Z ]{1,}$'
outlet_name_re = r'[a-zA-Z.0-9, ]{1,}[-_,]*[a-zA-Z.0-9 ]{1,}$'
web_re = r'[a-zA-Z]{1,}[:]{1,1}[//]{1,}[.a-zA-Z ]{1,}$'
username_re = r'[a-zA-Z.0-9& ]{1,}[-_& ]*[a-zA-Z.0-9& ]{1,}$'
product_re = r'[a-zA-Z.0-9 ]{1,}[-_&|,()" ]*[a-zA-Z.,0-9)&|" ]{1,}$'
pass_re = r'[a-zA-Z0-9-#$%^&*@!+_></\| ():;]{1,}$'
active_re = r'[01]{1,1}$'


def strtotime(t):
	time_only = datetime.strptime(t,'%Y-%m-%d')
	return time_only


def validate_anything(field_to_validate, reg_re, zero_re,minimum_len, field_name):
	a = ""
	if field_to_validate != "":
		if "^" in field_to_validate:
			a = "Please enter valid " +  field_name + "!!"
		if field_to_validate != None and len(field_to_validate)<minimum_len:
			a = field_name + " field should contain at least " + str(minimum_len) + " characters!!"
		if field_to_validate != None and re.match(zero__re, field_to_validate)\
											  and len(field_to_validate)>minimum_len-1:
			a = "All zeros are not allowed in " +field_name +" field!!"
		if field_to_validate != None and not re.match(zero__re, field_to_validate)\
				and len(field_to_validate)>minimum_len-1 and not re.match(reg_re, field_to_validate):
			a = "Please enter valid " +  field_name + "!!"
	else:
		pass
	if a == "":
		pass
	else:
		return a


def validate_exact(field_to_validate, reg_re, zero_re,exact_len, field_name):
	a = ""
	if "^" in field_to_validate:
		a = "Please enter valid " + field_name + "!!"
	if field_to_validate != None and len(field_to_validate)<exact_len:
		a = field_name + " field should contain exactly " + str(exact_len) + " characters!!"
	if field_to_validate != None and len(field_to_validate)>exact_len:
		a = field_name + " field should contain exactly " + str(exact_len) + " characters!!"
	if field_to_validate != None and re.match(zero__re, field_to_validate)\
	and len(field_to_validate)==exact_len:
		a = "All zeros are not allowed in " +field_name +" field!!"
	if field_to_validate != None and not re.match(zero__re, field_to_validate)\
	and len(field_to_validate)<=exact_len and not re.match(reg_re, field_to_validate):
		a = "Please enter valid " + field_name + "!!"
	if a == "":
		pass
	else:
		return a


def only_required(key_to_validate, alert_field_name):
	if key_to_validate==None or key_to_validate=="" or key_to_validate=="Null":
		only_response = "Please enter your " + alert_field_name +"!!"
	else:
		only_response = ""
	if only_response == "":
		pass
	else:
		return only_response

def validation_master_anything(key_to_validate, alert_field_name, reg_re, min_length):
	if key_to_validate==None or key_to_validate=="":
		response = "Please enter your " + alert_field_name +"!!"
	else:
		response = validate_anything(key_to_validate, reg_re, zero__re,
												 min_length, alert_field_name)
	if response == "":
		pass
	else:
		return response

def validation_master_exact(key_to_validate, alert_field_name,reg_re, exact_length):
	if key_to_validate==None or key_to_validate=="":
		response_exact = "Please enter your " + alert_field_name +"!!"
	else:
		response_exact = validate_exact(key_to_validate, reg_re, zero__re,
												 exact_length, alert_field_name)
	if response_exact == "":
		pass
	else:
		return response_exact



def universal_validation(**kwargs):
	err_message = {}
	for key, value in kwargs.items():
		err_message[key] = only_required(value,key)
	return err_message


def weekday_to_name(day_number):
	week_name = ["","Sunday","Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]
	day_name = week_name[day_number]
	return day_name



def otp_generator(size=7, chars=string.ascii_uppercase + string.digits):
	import random
	return ''.join(random.choice(chars) for _ in range(size))



def all_week_name():
	week_list = []
	week_data = {}
	week_data[0] = "Monday"
	week_data[1] = "Tuesday"
	week_data[2] = "Wednesday"
	week_data[3] = "Thursday"
	week_data[4] = "Friday"
	week_data[5] = "Saturday"
	week_data[6] = "Sunday"
	week_list.append(week_data)
	return week_list

def all_month_name():
	month_list = []
	month_data = {}
	month_data[0] = "January"
	month_data[1] = "February"
	month_data[2] = "March"
	month_data[3] = "April"
	month_data[4] = "May"
	month_data[5] = "June"
	month_data[6] = "July"
	month_data[7] = "August"
	month_data[8] = "September"
	month_data[9] = "October"
	month_data[10] = "November"
	month_data[11] = "December"
	month_list.append(month_data)
	return month_list