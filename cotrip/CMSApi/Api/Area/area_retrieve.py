from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
import re
from rest_framework.permissions import IsAuthenticated
from MappleApi.api_packages import *
import json
from datetime import datetime
#Serializer for api
from rest_framework import serializers
from Book.models import MstAreas
from datetime import datetime, timedelta



class AreaSerializer(serializers.ModelSerializer):
	class Meta:
		model = MstAreas
		fields = '__all__'


class AreaRetrieve(APIView):
	"""
	Area retrieval POST API

		Authentication Required		: Yes
		Service Usage & Description	: This Api is used for retrieval of Area data.

		Data Post: {
			"id"                   : "1"
		}

		Response: {

			"success": True, 
			"message": "Area retrieval api worked well!!",
			"data": final_result
		}

	"""
	permission_classes = (IsAuthenticated,)
	def post(self, request, format=None):
		try:
			data = request.data
			err_message = {}
			err_message["id"] = \
					validation_master_anything(data["id"],
					"Area Id",contact_re, 1)
			if any(err_message.values())==True:
				return Response({
					"success": False,
					"error" : err_message,
					"message" : "Please correct listed errors!!"
					})
			record = MstAreas.objects.filter(id=data['id'])
			if record.count() == 0:
				return Response(
				{
					"success": False,
 					"message": "Provided Coupon data is not valid to retrieve!!"
				}
				)
			else:
				final_result = []
				q_dict = {}
				q_dict["id"] = record[0].id
				q_dict["area_name"] = record[0].area_name
				q_dict["sort"] = record[0].sort
				if record[0].draft ==str(0):
					q_dict["draft"] = "Unpublished"
				elif record[0].draft == str(1):
					q_dict["draft"] = "Editing"
				else:
					q_dict["draft"] = "Release"

				if record[0].oversea == False:
					q_dict["oversea"] = str(0)
				else:
					q_dict['oversea'] = str(1)
				q_dict["revision"] = record[0].revision
				q_dict["area_code"] = record[0].area_code
				q_dict["status"] = record[0].status
				if record[0].modified !=None:
					m = record[0].modified+timedelta(hours=5,minutes=30)
					q_dict["modified"] =  m.strftime("%Y-%m-%d %I:%M %p")
				else:
					q_dict["modified"] = ''
				p = record[0].created+timedelta(hours=5,minutes=30)
				q_dict['registration'] = p.strftime("%Y-%m-%d %I:%M %p")


				final_result.append(q_dict)
			if final_result:
				return Response({
							"success": True, 
							"message": "Area retrieval api worked well!!",
							"data": final_result,
							})
			else:
				return Response({
							"success": True, 
							"message": "No Area data found!!"
							})
		except Exception as e:
			print("Area retrieval Api Stucked into exception!!")
			print(e)
			return Response({"success": False, "message": "Error happened!!", "errors": str(e)})