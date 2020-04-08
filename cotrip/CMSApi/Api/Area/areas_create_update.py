import re
import json
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from MappleApi.api_packages import *
from datetime import datetime
from django.db.models import Q
import os
from django.db.models import Max

#Serializer for api
from rest_framework import serializers
from Book.models import MstAreas

class AreaSerializer(serializers.ModelSerializer):
	class Meta:
		model = MstAreas
		fields = '__all__'


class AreaCreationUpdation(APIView):
	"""
	Area Creation & Updation POST API

		Authentication Required		: Yes
		Service Usage & Description	: This Api is used to create & update area for cms.

		Data Post: {
			"id"                   : "1"(Send this key in update record case,else it is not required!!)
			"oversea"		       : "0",(1=oversea,0=domestic)
			"area_name"		       : "delhi",
			"area_code" 	       : "wewrw",
			"status"               : "0" (0=Disable,a=enable)
		}

		Response: {

			"success": True, 
			"message": "Area creation/updation api worked well!!",
			"data": final_result
		}

	"""
	permission_classes = (IsAuthenticated,)
	def post(self, request, format=None):
		try:
			data = request.data
			print("fffffffff",data)
			err_message = {}
			data['draft'] = 0
			err_message["area_name"] =  validation_master_anything(
									data["area_name"],
									"Area name", username_re, 3)

			err_message["area_code"] =  validation_master_anything(
									data["area_code"],
									"Area code", vat_re, 3)

			if any(err_message.values())==True:
				return Response({
					"success": False,
					"error" : err_message,
					"message" : "Please correct listed errors!!"
					})

			if "id" in data:
				print("dddddddddddd",data)
				area_record = MstAreas.objects.filter(id=data['id'])
				if area_record.count() == 0:
					return Response(
					{
						"success": False,
	 					"message": "Area data is not valid to update!!"
					}
					)
				else:
					data["modified"] = datetime.now()
					area_serializer = AreaSerializer(area_record[0],data=data,partial=True)
					if area_serializer.is_valid():
						data_info = area_serializer.save()
					else:
						print("something went wrong!!")
						return Response({
							"success": False, 
							"message": str(area_serializer.errors),
							})
			else:
				area_serializer = AreaSerializer(data=data)
				if area_serializer.is_valid():
					data_info = area_serializer.save()
				else:
					print("something went wrong!!")
					return Response({
						"success": False, 
						"message": str(area_serializer.errors),
						})
			final_result = []
			final_result.append(area_serializer.data)
			return Response({
						"success": True, 
						"message": "Area creation/updation api worked well!!",
						"data": final_result,
						})
		except Exception as e:
			print("Area creation/updation Api Stucked into exception!!")
			print(e)
			return Response({"success": False, "message": "Error happened!!", "errors": str(e)})

