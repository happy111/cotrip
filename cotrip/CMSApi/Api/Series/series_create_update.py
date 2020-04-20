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
from Book.models import MstSeries

class SeriesSerializer(serializers.ModelSerializer):
	class Meta:
		model = MstSeries
		fields = '__all__'


class SeriesCreationUpdation(APIView):
	"""
	Series Creation & Updation POST API

		Authentication Required		: Yes
		Service Usage & Description	: This Api is used to create & update series for cms.

		Data Post: {
			"id"                   : "1"(Send this key in update record case,else it is not required!!)
			"series_name"		   : "Pizza",
			"series_code"		   : "123456",
			"oversea"		       : "0",(1=oversea,0=domestic)
			"status"               : "0" (0=Disable,a=enable)
		}

		Response: {

			"success": True, 
			"message": "Area creation/updation api worked well!!",
			"data": final_result
		}

	"""
	# permission_classes = (IsAuthenticated,)
	def post(self, request, format=None):
		try:
			data = request.data
			# err_message = {}
			# err_message["series_name"] =  validation_master_anything(
			# 						data["series_name"],
			# 						"Series name", username_re, 1)

			# err_message["series_code"] =  validation_master_anything(
			# 						data["series_code"],
			# 						"Series code", vat_re, 1)

			# if any(err_message.values())==True:
			# 	return Response({
			# 		"success": False,
			# 		"error" : err_message,
			# 		"message" : "Please correct listed errors!!"
			# 		})



			if "id" in data:
				series_record = MstSeries.objects.filter(id=data['id'])
				if series_record.count() == 0:
					return Response(
					{
						"success": False,
	 					"message": "Series data is not valid to update!!"
					}
					)
				else:
					data["modified"] = datetime.now()
					series_serializer = SeriesSerializer(series_record[0],data=data,partial=True)
					if series_serializer.is_valid():
						data_info = series_serializer.save()
					else:
						print("something went wrong!!")
						return Response({
							"success": False, 
							"message": str(series_serializer.errors),
							})
			else:
				data['draft'] = 0
				data['status'] = 1
				series_serializer = SeriesSerializer(data=data)
				if series_serializer.is_valid():
					data_info = series_serializer.save()
				else:
					print("something went wrong!!")
					return Response({
						"success": False, 
						"message": str(series_serializer.errors),
						})
			final_result = []
			final_result.append(series_serializer.data)
			return Response({
						"success": True, 
						"message": "Series creation/updation api worked well!!",
						"data": final_result,
						})
		except Exception as e:
			print("Series creation/updation Api Stucked into exception!!")
			print(e)
			return Response({"success": False, "message": "Error happened!!", "errors": str(e)})

