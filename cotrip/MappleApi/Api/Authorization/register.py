import re
import dateutil.parser
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from MappleApi.api_packages import *
from rest_framework_tracking.mixins import LoggingMixin
from django.contrib.sites.shortcuts import get_current_site
from django.utils.encoding import force_bytes, force_text
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.html import strip_tags
from _thread import start_new_thread
from django.db.models import Q
from Customers.models import CustomerProfile
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout

class CustomerSignUpSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomerProfile
		fields = '__all__'



class Profile(LoggingMixin,APIView):
	"""
	Customer Profile update POST API

		Authentication Required		: Yes
		Service Usage & Description	: This Api is used to customer Profile update for Mapple
		{
			"nickname"			: "umesh",
			"birth_year"        : "2019-09-22",(y-m-d Formate)
			"gender"            : "male",
			"twitter_id"        : "abc"  (optional)
			"facebook_id"       : "abc"  (optional)
			"married"           : "0" (0= unmarried,1= married)
			"job"				: "Software developer",
			"prefecture"		: "delhi",
			"allow_mail"        : "0"(0= not allow,1=allolw)
			
		}

		Response:{
			    "success": true,
			    "data": {
			        "id": 28,
			        "nickname": "umesh",
			        "prefecture": "delhi",
			        "username": "1Mramesh@gmail.com",
			        "mobile": null,
			        "user_type": false,
			        "email": "ramesh@gmail.com",
			        "gender": "male",
			        "birth_year": "2000-09-22T00:00:00Z",
			        "age": 19,
			        "twitter_id": "abc",
			        "facebook_id": "abc",
			        "married": false,
			        "job": "dasdas",
			        "allow_mail": false,
			        "active_status": false,
			        "created_at": "2020-03-27T04:31:38.636572Z",
			        "updated_at": null,
			        "last_logined": null,
			        "deleted": null,
			        "auth_user": 16,
			        "company": 1
			    },
			    "message": "Profile Updated successfully.!!"
}
			}

	"""
	permission_classes = (IsAuthenticated,)
	def post(self, request, format=None):
		try:
			registration_data = request.data
			user_id = request.user.id
			mutable = request.POST._mutable
			request.POST._mutable = True
			err_message = {}
			registration_data['email'] = request.user.email
			err_message["nickname"] = \
					validation_master_anything(registration_data["nickname"],
					"Nick Name",username_re, 1)
			err_message["prefecture"] = \
					validation_master_anything(registration_data["prefecture"],
					"State",username_re, 1)
			err_message["job"] = \
					validation_master_anything(registration_data["job"],
					"Job title",username_re, 1)
			
			if type(registration_data['birth_year']) == str and registration_data['birth_year'] == '':
				err_message["birth_year"]  = "Please Enter date of birth!!"
			else:
				dbirth = dateutil.parser.parse(registration_data["birth_year"])
				now = datetime.now()
				today = now.date()
				date_format = "%Y-%m-%d"
				dbirths = dbirth.date()
				t1 = datetime.strptime(str(today),date_format)
				t2 = datetime.strptime(str(dbirths),date_format)
				diff = t1-t2
				days = diff.days
				if days > 6570:
					registration_data["age"] = days // 365
				else:
					err_message['age'] = "Age is not Valid!!"
			if any(err_message.values())==True:
				return Response({
					"error" : err_message,
					"message" : "Please correct listed errors!!"
					})
			registration_data['company'] = str(1)
			username = registration_data['company'] +'M'+str(registration_data['email'])
			if registration_data["birth_year"]:
				s = "00:00:00.000000"
				registration_data["birth_year"] = registration_data["birth_year"] +" "+ s
			else:
				pass
			cusdata = CustomerProfile.objects.filter(email=registration_data['email'])
			if cusdata.count() > 0:
				registration_data["username"] = username
				registration_data["user_type"] = 0

				customer_registration_serializer = CustomerSignUpSerializer(cusdata[0],data=registration_data,partial=True)
				if customer_registration_serializer.is_valid():
					customer_data_save = customer_registration_serializer.save()
					self.authuserId = request.user.id
					userData = User.objects.filter(id=self.authuserId).first()
					if userData:
						request.user.auth_token.delete()
						logout(request)
					return Response(
								{
						"success": True,
						"data" : customer_registration_serializer.data,
						"message": "Profile Updated  successfully.!!"
								}
							 	)
			else:
				registration_data["auth_user"] = user_id
				registration_data["username"] = username
				registration_data["user_type"] = 0
				customer_registration_serializer = CustomerSignUpSerializer(data=registration_data)
				if customer_registration_serializer.is_valid():
					customer_data_save = customer_registration_serializer.save()
					self.authuserId = request.user.id
					userData = User.objects.filter(id=self.authuserId).first()
					if userData:
						request.user.auth_token.delete()
						logout(request)
					return Response(
								{
						"success": True,
						"data" : customer_registration_serializer.data,
						"message": "Profile Updated successfully.!!"
								}
							 	)
				else:
					return Response(
						{
							"success": False, "message": str(customer_registration_serializer.errors)
						}
					)

		except Exception as e:
			print("Registration Api Stucked into exception!!")
			print(e)
			return Response({"success": False, "message": "Error happened!!", "errors": str(e)})

