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
		Service Usage & Description	: This Api is used to provide login services to user on the basis of provided user_id.

		Data Post: {

			"user_id"			        : "72"
		}

		Response: {

			"credential"			: true,
			"token"                 : "zctebjfndfjwhjsbdewbdewzzzz"

		}

	"""
	
	# permission_classes = (IsAuthenticated,)
	def post(self, request, format=None):
		try:
			data = request.data
			err_message = {}
			err_message["email"] =  validation_master_anything(
									str(data["user_id"]),
									"Email", contact_re, 1)
			if any(err_message.values())==True:
				return Response({
					"success": False,
					"error" : err_message,
					"message" : "Please correct listed errors!!"
					})
			username = str(data["user_id"])
			check_user = User.objects.filter(username=username)
			if check_user.count() == 1:
				data["password"] = "!!!!!!"
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
					return Response({
						"success": True,
						"credential" : True,
						"token": token.key
						})
				else:
					return Response({
						"success": False,
						"credential" : False,
						"message": "Please enter valid login credentials!!"
						})
		except Exception as e:
			print("User Login Api based on user_id Stucked into exception!!")
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