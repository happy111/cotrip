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
from django.contrib.auth import authenticate, login
from MappleApi.api_packages import *
from rest_framework.authtoken.models import Token
class CustomerSignUpSerializer(serializers.ModelSerializer):
	class Meta:
		model = CustomerProfile
		fields = '__all__'


class Signup(LoggingMixin,APIView):
	"""
	This Api is used tp provide basic signup/signin functionality on mapple

		Authentication Required		: No
		Service Usage & Description	: This Api is used to customer Signup / Signin for Mapple
		{
			
			"email"             : "umeshsamal3@gmail.com",
			"password"			: "123456",
		}
		Response: {
			    "success": true,
			    "credential": true,
			    "message": "You have been  login successfully.!!",
			    "token": "e5d5effea8c5cc0edb8b4fa89241207a9546a23f",
			    "user_id": 14
			}
	"""

	def post(self, request, format=None):
		try:
			registration_data = request.data
			mutable = request.POST._mutable
			request.POST._mutable = True
			err_message = {}
			r_data = {}
			la = {}
			err_message["email"] = \
					validation_master_anything(registration_data["email"],
					"Email",email_re, 3)

			err_message["password"] = \
					validation_master_anything(registration_data["password"],
					"Password", vat_re, 6)
			
			if any(err_message.values())==True:
				return Response({
					"error" : err_message,
					"message" : "Please correct listed errors!!"
					})

			registration_data['company'] = str(1)
			username = registration_data['company'] +'M'+str(registration_data['email'])
			email = registration_data['email']
			email_already_exist = User.objects.filter(email=email)
			if email_already_exist.count()==1:
				user_authenticate = authenticate(username=username,password=registration_data['password'])
				if user_authenticate == None:
					return Response({
						"success": False,
						"credential" : False,
						"message": "Your account is not activated or password not match!!"
						})
				else:
					if user_authenticate and user_authenticate.is_active == True \
										and user_authenticate.is_staff==False\
										and user_authenticate.is_superuser == False:
						login(request,user_authenticate)
						token, created = Token.objects.get_or_create(user=user_authenticate)
						user_id = token.user_id
						cusdata = CustomerProfile.objects.filter(auth_user_id=user_id)
						la['last_logined'] =  datetime.now()
						customer_registration_serializer = CustomerSignUpSerializer(cusdata[0],data=la,partial=True)
						if customer_registration_serializer.is_valid():
							customer_data_save = customer_registration_serializer.save()
						return Response({
								"success": True,
								"credential" : True,
								"message" : "You have been  login successfully.!!",
								"token": token.key,
								"user_id" : user_id,
								})

			else:
				create_user = User.objects.create_user(
							username=username,
							email=email,
							password=registration_data['password'],
							is_staff=False,
							is_active=True
							)
				if create_user:
					r_data['password'] = registration_data['password']
					r_data["auth_user"] = create_user.id
					r_data["user_type"] = 0
					r_data["email"] = registration_data['email']
					customer_registration_serializer = CustomerSignUpSerializer(data=r_data)
					if customer_registration_serializer.is_valid():
						customer_data_save = customer_registration_serializer.save()
					else:
						print("Error",customer_registration_serializer)
					user_authenticate = authenticate(username=username,password=registration_data['password'])
					if user_authenticate == None:
						return Response({
							"success": False,
							"credential" : False,
							"message": "Your account is not activated or password not match!!"
							})
					else:
						pass
					if user_authenticate and user_authenticate.is_active == True \
											and user_authenticate.is_staff==False\
											and user_authenticate.is_superuser == False:
						login(request,user_authenticate)
						token, created = Token.objects.get_or_create(user=user_authenticate)
						user_id = token.user_id
						return Response({
							"success": True,
							"credential" : True,
							"message" : "You have been registered successfully.!!",
							"token": token.key,
							"user_id" : user_id,
							})
					else:
						pass
				else:
					pass
		except Exception as e:
			print("Registration Api Stucked into exception!!")
			print(e)
			return Response({"success": False, "message": "Error happened!!", "errors": str(e)})

