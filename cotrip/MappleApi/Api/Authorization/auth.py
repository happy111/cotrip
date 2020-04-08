import re
import datetime
from rest_framework.views import APIView
from rest_framework.response import Response
from Brands.models import Company
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from MappleApi.api_packages import *
from rest_framework.authtoken.models import Token
from rest_framework.permissions import IsAuthenticated
from django.contrib.auth import logout
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from Customers.models import CustomerProfile
from rest_framework_tracking.mixins import LoggingMixin

class Login(LoggingMixin,APIView):

	"""	
	Customer login POST API

		Authentication Required		: No
		Service Usage & Description	: This Api is used to provide login services to user.

		Data Post: {

			"email"			        : "umeshsamal3@gmail.com",
			"password"		        : "123456"
		}

		Response: {

			"credential"			: true,
			"message"				: "You are logged in now!!",

		}

	"""
	
	# permission_classes = (IsAuthenticated,)
	def post(self, request, format=None):
		try:
			data = request.data
			err_message = {}
			err_message["email"] =  validation_master_anything(
									data["email"],
									"Email", email_re, 3)
			err_message["password"] =  only_required(data["password"],"Password")
			if any(err_message.values())==True:
				return Response({
					"success": False,
					"error" : err_message,
					"message" : "Please correct listed errors!!"
					})

			data['company'] = str(1)
			username = data['company'] +'M'+str(data['email'])
			is_user = CustomerProfile.objects.filter(username=username)
			if is_user.count()==1:
				if is_user.first().active_status == 0:
					return Response({
					"success" : False,
					"message" : "User account is not active..Please contact admin!!"
					})
				else:
					pass
				credential_check = \
					is_user.filter(password=data['password'])
				if credential_check.count() == 1:
					pass
				else:
					return Response \
						({
						"success": False,
						"credential" : False,
						"message": \
						"Please enter valid login credentials!!"
						})
				user_authenticate = authenticate(username=username,password=data['password'])
				if user_authenticate == None:
					return Response({
						"success": False,
						"credential" : False,
						"message": "Your account is not activated!!"
						})
				else:
					pass
				if user_authenticate and user_authenticate.is_active == True \
										and user_authenticate.is_staff==False\
										and user_authenticate.is_superuser == False:
					login(request,user_authenticate)
					token, created = Token.objects.get_or_create(user=user_authenticate)
					user_id = token.user_id
					user_type = is_user[0].user_type
					if user_type == str(0):
						utype = "Normal User"
					else:
						utype = 'Admin'
					return Response({
						"success": True,
						"credential" : True,
						"message" : "You are logged in now!!",
						"token": token.key,
						"user_id" : user_id,
						"user_type": utype
						})
				else:
					return Response({
						"success": False,
						"credential" : False,
						"message": "Please enter valid login credentials!!"
						})
			else:
				return Response({
						"success": False,
						"credential" : False,
						"message": "This Username does not exist in the system!!"
						})
		except Exception as e:
			print("User Login Api Stucked into exception!!")
			print(e)
			return Response({"success": False, "message": "Error happened!!", "errors": str(e)})



class Logout(APIView):
	"""
	User logout POST API

		Authentication Required		: Yes
		Service Usage & Description	: This Api is used to provide logout service to user..

		Data Post: {

			"token": "95dabfce1f8ebe9331851a1a1c5aa22bcb9b8120"
		}

		Response: {

			"success": True,
			"message" : "You have been successfully logged out!!"
		}

	"""
	permission_classes = (IsAuthenticated,)
	def post(self, request, format=None):
		try:
			self.authuserId = request.user.id
			userData = User.objects.filter(id=self.authuserId).first()
			if userData:
				request.user.auth_token.delete()
				logout(request)
				return Response({
							"success": True,
							"message": "You have been successfully logged out!!",
							})
			else:
				return Response({
							"success": False,
							"message": "User not Found!!",
							})
		except Exception as e:
			print(e)
			return Response({"success": False, "message": "Error happened!!", "errors": str(e)})